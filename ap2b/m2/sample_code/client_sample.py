import requests

BASE_URL = "https://whitelobster.onpella.app/mahasiswa"

def create_mahasiswa(data):
    response = requests.post(BASE_URL, json=data)
    try:
        print("Create Response:", response.json())
    except Exception:
        print("Create Error:", response.status_code, response.text)

def get_mahasiswa():
    response = requests.get(BASE_URL)
    try:
        print("Get All Mahasiswa:", response.json())
    except Exception:
        print("Get Error:", response.status_code, response.text)

def get_mahasiswa_by_npm(npm):
    response = requests.get(f"{BASE_URL}/{npm}")
    try:
        print(f"Get Mahasiswa with NPM {npm}:", response.json())
    except Exception:
        print("Get by NPM Error:", response.status_code, response.text)

def update_mahasiswa(npm, data):
    response = requests.put(f"{BASE_URL}/{npm}", json=data)
    try:
        print(f"Update Mahasiswa with NPM {npm}:", response.json())
    except Exception:
        print("Update Error:", response.status_code, response.text)

def delete_mahasiswa(npm):
    response = requests.delete(f"{BASE_URL}/{npm}")
    try:
        print(f"Delete Mahasiswa with NPM {npm}:", response.json())
    except Exception:
        print("Delete Error:", response.status_code, response.text)

new_mahasiswa = {
    "npm": "50422742",
    "nama": "Jessica Valencia",
    "kelas": "3IA01",
    "jurusan": "Teknik Informatika"
}

create_mahasiswa(new_mahasiswa)
get_mahasiswa()
get_mahasiswa_by_npm("50422742")

update_data = {
    "npm": "50422742",
    "nama": "Jessica Valencia Chow",
    "kelas": "3IA01",
    "jurusan": "Teknik Informatika"
}
update_mahasiswa("50422742", update_data)
get_mahasiswa_by_npm("50422742")

delete_mahasiswa("50422742")
get_mahasiswa()
