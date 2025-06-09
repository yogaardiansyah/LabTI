import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

rekening_db = {
    "111222333": {"nama_pemilik": "Andi Pratama", "saldo": 5000000},
    "444555666": {"nama_pemilik": "Bunga Lestari", "saldo": 10000000},
    "777888999": {"nama_pemilik": "Charlie Wijaya", "saldo": 2500000},
    "123123123": {"nama_pemilik": "Diana Putri", "saldo": 75000000},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-BDN] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/rekening/<nomor_rekening>/saldo', methods=['GET'])
def get_saldo(nomor_rekening):
    """Endpoint untuk mendapatkan saldo berdasarkan nomor rekening."""
    log_server_activity(f"Permintaan saldo untuk rekening: {nomor_rekening}")
    
    time.sleep(random.uniform(0.1, 0.5)) 
    
    with db_lock:
        rekening = rekening_db.get(nomor_rekening)
    
    if rekening:
        return jsonify({
            "nomor_rekening": nomor_rekening, 
            "nama_pemilik": rekening["nama_pemilik"], 
            "saldo": rekening["saldo"]
        }), 200
    else:
        return jsonify({"error": "Rekening tidak ditemukan"}), 404

@app.route('/transfer', methods=['POST'])
def transfer_dana():
    data = request.get_json()
    rekening_sumber = data.get('rekening_sumber')
    rekening_tujuan = data.get('rekening_tujuan')
    jumlah = data.get('jumlah')
    log_server_activity(f"Menerima permintaan transfer dari {rekening_sumber} ke {rekening_tujuan} sejumlah {jumlah}")
    if not all([rekening_sumber, rekening_tujuan, jumlah]):
        return jsonify({"error": "Data transfer tidak lengkap"}), 400
    return jsonify({"message": "Fungsi transfer ada, tapi tidak diuji oleh klien dalam soal ini."}), 200


if __name__ == '__main__':
    log_server_activity("Bank Digital Nusantara API Server (Mode Sederhana) dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)