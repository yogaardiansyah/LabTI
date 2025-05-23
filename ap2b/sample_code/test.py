import pytest
from app import create_app
from app.models import topup_data
import json

API_KEY = "actm7"
API_PREFIX = "/api"

@pytest.fixture(scope="function")
def client():
    app = create_app()
    app.config["TESTING"] = True

    topup_data.clear()

    with app.test_client() as client:
        yield client
    
    topup_data.clear()

def test_health_check(client):
    response = client.get(f"{API_PREFIX}/health")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "sehat"

def test_header_cors(client):
    response = client.get(f"{API_PREFIX}/topup", headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert "Access-Control-Allow-Origin" in response.headers
    assert response.headers["Access-Control-Allow-Origin"] == "*"

def test_api_key_diperlukan(client):
    response = client.get(f"{API_PREFIX}/topup")
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data["error"] == "Tidak berwenang"

    response = client.get(f"{API_PREFIX}/topup", headers={"X-API-Key": "wrong-key"})
    assert response.status_code == 401

    response = client.get(f"{API_PREFIX}/topup", headers={"X-API-Key": API_KEY})
    assert response.status_code == 200

def test_batas_rate_limit(client):
    limit_count = 10
    limit_string_expected = f"{limit_count} per 15 second"

    headers = {"X-API-Key": API_KEY}
    for i in range(limit_count):
        response = client.get(f"{API_PREFIX}/topup", headers=headers)
        assert response.status_code == 200, f"Request {i+1} gagal, seharusnya berhasil."
    
    response_over_limit = client.get(f"{API_PREFIX}/topup", headers=headers)
    assert response_over_limit.status_code == 429
    data = json.loads(response_over_limit.data)
    assert data["error"] == "batas permintaan terlampaui"
    assert data["message"] == limit_string_expected
    assert data["limit"] == limit_string_expected



def test_ambil_semua_topup_awal_kosong(client):
    response = client.get(f"{API_PREFIX}/topup", headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) == 0

def test_tambah_topup(client):
    topup_baru = {"user": "alice", "amount": 10000}
    response_post = client.post(
        f"{API_PREFIX}/topup",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json=topup_baru
    )
    assert response_post.status_code == 201
    data_post = json.loads(response_post.data)
    assert data_post["message"] == "Topup berhasil ditambahkan"
    assert data_post["data"]["user"] == "alice"

    response_get = client.get(f"{API_PREFIX}/topup", headers={"X-API-Key": API_KEY})
    data_get = json.loads(response_get.data)
    assert len(data_get) == 1
    assert data_get[0]["user"] == "alice"
    assert data_get[0]["amount"] == 10000

def test_tambah_topup_payload_tidak_lengkap(client):
    topup_invalid = {"user": "bad_user"}
    response = client.post(
        f"{API_PREFIX}/topup",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json=topup_invalid
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["error"] == "Data user atau jumlah tidak lengkap"

def test_perbarui_topup(client):
    topup_awal = {"user": "bob", "amount": 20000}
    client.post(
        f"{API_PREFIX}/topup",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json=topup_awal
    )

    data_update = {"user": "bob_diperbarui", "amount": 30000}
    response_put = client.put(
        f"{API_PREFIX}/topup/0",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json=data_update
    )
    assert response_put.status_code == 200
    data_put = json.loads(response_put.data)
    assert data_put["message"] == "Topup berhasil diperbarui"
    assert data_put["data"]["user"] == "bob_diperbarui"
    assert data_put["data"]["amount"] == 30000

    response_get = client.get(f"{API_PREFIX}/topup/0", headers={"X-API-Key": API_KEY})
    response_get_all = client.get(f"{API_PREFIX}/topup", headers={"X-API-Key": API_KEY})
    data_get_all = json.loads(response_get_all.data)
    assert data_get_all[0]["user"] == "bob_diperbarui"


    response_put_notfound = client.put(
        f"{API_PREFIX}/topup/999",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json=data_update
    )
    assert response_put_notfound.status_code == 404
    data_notfound = json.loads(response_put_notfound.data)
    assert data_notfound["error"] == "Data tidak ditemukan"

def test_perbarui_topup_payload_tidak_lengkap(client):
    client.post(f"{API_PREFIX}/topup", headers={"X-API-Key": API_KEY, "Content-Type": "application/json"}, json={"user": "cek_update", "amount": 100})

    data_update_invalid = {"user": "user_saja"}
    response = client.put(
        f"{API_PREFIX}/topup/0",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json=data_update_invalid
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["error"] == "Data user atau jumlah tidak lengkap"

def test_hapus_topup(client):
    topup_awal = {"user": "charlie", "amount": 15000}
    client.post(
        f"{API_PREFIX}/topup",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json=topup_awal
    )

    response_delete = client.delete(f"{API_PREFIX}/topup/0", headers={"X-API-Key": API_KEY})
    assert response_delete.status_code == 200
    data_delete = json.loads(response_delete.data)
    assert data_delete["message"] == "Topup berhasil dihapus"
    assert data_delete["data_terhapus"]["user"] == "charlie"

    response_get = client.get(f"{API_PREFIX}/topup", headers={"X-API-Key": API_KEY})
    data_get = json.loads(response_get.data)
    assert len(data_get) == 0

    response_delete_notfound = client.delete(f"{API_PREFIX}/topup/999", headers={"X-API-Key": API_KEY})
    assert response_delete_notfound.status_code == 404
    data_notfound = json.loads(response_delete_notfound.data)
    assert data_notfound["error"] == "Data tidak ditemukan"