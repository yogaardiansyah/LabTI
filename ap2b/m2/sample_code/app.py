"""Aplikasi Flask sederhana untuk CRUD data mahasiswa."""

from flask import Flask, request, jsonify

app = Flask(__name__)

mahasiswa_db = [
    {
        "npm": "51422643",
        "nama": "Yoga Ardiansyah",
        "kelas": "3IA25",
        "jurusan": "Teknik Informatika"
    }
]

@app.route('/mahasiswa', methods=['POST'])
def create_mahasiswa():
    """Membuat entri data mahasiswa baru."""
    data = request.get_json()
    for m in mahasiswa_db:
        if m['npm'] == data.get('npm'):
            return jsonify({'error': 'Mahasiswa dengan NPM tersebut sudah ada'}), 409

    if not all(k in data for k in ['npm', 'nama', 'kelas', 'jurusan']):
        return jsonify({'error': 'Data tidak lengkap'}), 400

    mahasiswa_db.append(data)
    return jsonify(data), 201

@app.route('/mahasiswa', methods=['GET'])
def get_all_mahasiswa():
    """Mengambil seluruh data mahasiswa."""
    return jsonify(mahasiswa_db), 200

@app.route('/mahasiswa/<npm>', methods=['GET'])
def get_mahasiswa(npm):
    """Mengambil data mahasiswa berdasarkan NPM."""
    for m in mahasiswa_db:
        if m['npm'] == npm:
            return jsonify(m), 200
    return jsonify({'error': 'Mahasiswa tidak ditemukan'}), 404

@app.route('/mahasiswa/<npm>', methods=['PUT'])
def update_mahasiswa(npm):
    """Memperbarui data mahasiswa berdasarkan NPM."""
    data = request.get_json()
    for i, m in enumerate(mahasiswa_db):
        if m['npm'] == npm:
            if not all(k in data for k in ['npm', 'nama', 'kelas', 'jurusan']):
                return jsonify({'error': 'Data tidak lengkap'}), 400
            mahasiswa_db[i] = data
            return jsonify(data), 200
    return jsonify({'error': 'Mahasiswa tidak ditemukan'}), 404

@app.route('/mahasiswa/<npm>', methods=['DELETE'])
def delete_mahasiswa(npm):
    """Menghapus data mahasiswa berdasarkan NPM."""
    for i, m in enumerate(mahasiswa_db):
        if m['npm'] == npm:
            deleted = mahasiswa_db.pop(i)
            return jsonify(deleted), 200
    return jsonify({'error': 'Mahasiswa tidak ditemukan'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
