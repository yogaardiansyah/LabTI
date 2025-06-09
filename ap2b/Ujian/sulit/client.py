import requests
import time

BASE_URL = "http://127.0.0.1:5001/nasabah"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Nasabah Fintech...")

    nasabah_baru_1 = {"id_nasabah": "FMJ101", "nama_lengkap": "Alice Wonderland", "tipe_akun": "Platinum", "saldo_awal": 10000000}
    nasabah_baru_2 = {"id_nasabah": "FMJ102", "nama_lengkap": "Bob The Builder", "tipe_akun": "Gold", "saldo_awal": 5000000}
    nasabah_tidak_lengkap = {"id_nasabah": "FMJ103", "nama_lengkap": "Charlie Brown"}

    print_response(requests.post(BASE_URL, json=nasabah_baru_1), "Create Nasabah 1 (Alice)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=nasabah_baru_2), "Create Nasabah 2 (Bob)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=nasabah_baru_1), "Create Nasabah 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=nasabah_tidak_lengkap), "Create Nasabah Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Nasabah (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/FMJ101"), "Get Nasabah FMJ101 (Alice)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/FMJ999"), "Get Nasabah FMJ999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_alice = {"nama_lengkap": "Alice In Chains", "tipe_akun": "Diamond", "saldo_awal": 12000000}
    update_data_tidak_lengkap = {"nama_lengkap": "Bob Updated"}

    print_response(requests.put(f"{BASE_URL}/FMJ101", json=update_data_alice), "Update Nasabah FMJ101 (Alice)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/FMJ102", json=update_data_tidak_lengkap), "Update Nasabah FMJ102 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/FMJ999", json=update_data_alice), "Update Nasabah FMJ999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/FMJ101"), "Get Nasabah FMJ101 (Setelah Update Alice)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/FMJ102"), "Delete Nasabah FMJ102 (Bob)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/FMJ999"), "Delete Nasabah FMJ999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/FMJ102"), "Get Nasabah FMJ102 (Setelah Delete Bob, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Nasabah (Setelah Delete)")

    print("\nPengujian Selesai.")