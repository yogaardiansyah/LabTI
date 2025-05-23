import requests
import json
import time

BASE_URL = "http://localhost:5000"
API_KEY = "actm7"

API_PREFIX = "/api"
TOPUP_ENDPOINT = f"{BASE_URL}{API_PREFIX}/topup"
HEALTH_ENDPOINT = f"{BASE_URL}{API_PREFIX}/health"

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}
def make_request(method, url, **kwargs):
    print(f"\nMencoba: {method.upper()} {url}")
    if 'json' in kwargs and 'headers' not in kwargs:
        kwargs['headers'] = headers
    elif 'headers' not in kwargs:
        kwargs['headers'] = {"X-API-Key": API_KEY}

    try:
        resp = requests.request(method, url, **kwargs)
        print(f"Status respons: {resp.status_code}")
        try:
            print("Isi respons JSON:")
            print(json.dumps(resp.json(), indent=2))
        except requests.exceptions.JSONDecodeError:
            print("Isi respons teks:")
            print(resp.text)
        return resp
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR: Tidak dapat terhubung ke {url}. Apakah server sudah berjalan? ({e})")
        return None
    except Exception as e:
        print(f"Terjadi kesalahan tak terduga: {e}")
        return None

if __name__ == "__main__":
    print("Client mulai...")

    print("\n--- Memeriksa status server (tanpa API key, tanpa rate limit) ---")
    make_request("get", HEALTH_ENDPOINT, headers={})
    time.sleep(0.5)

    print("\n--- Tes Create (harus kena batas rate limit setelah 3 permintaan sukses) ---")
    for i in range(5):
        create_resp = make_request(
            "post",
            TOPUP_ENDPOINT,
            json={"user": f"testuser{i+1}", "amount": 1000 + (i * 100)}
        )
        if create_resp and create_resp.status_code == 429:
            print("!!! SUDAH MENCAPAI BATAS RATE LIMIT !!!")
        time.sleep(0.5)

    print("\nMenunggu waktu rate limit selesai (16 detik)...")
    time.sleep(16)

    print("\n--- Tes Ambil Semua Setelah Tunggu (harus berhasil) ---")
    get_all_resp = make_request("get", TOPUP_ENDPOINT)

    if get_all_resp and get_all_resp.status_code == 200:
        topups = get_all_resp.json()
        if topups:
            print(f"\n--- Tes Update data pertama (idx 0) ---")
            make_request(
                "put",
                f"{TOPUP_ENDPOINT}/0",
                json={"user": "updated_user", "amount": 5000}
            )
            time.sleep(0.5)

            print("\n--- Tes Ambil Semua Setelah Update ---")
            make_request("get", TOPUP_ENDPOINT)
            time.sleep(0.5)

            print(f"\n--- Tes Hapus data pertama (idx 0) ---")
            make_request("delete", f"{TOPUP_ENDPOINT}/0")
            time.sleep(0.5)

            print("\n--- Tes Ambil Semua Setelah Hapus ---")
            make_request("get", TOPUP_ENDPOINT)
        else:
            print("\nTidak ada data topup untuk diuji update/hapus.")
    else:
        print("\nGagal mengambil data topup, tes berikutnya mungkin tidak relevan.")

    print("\nClient selesai.")
