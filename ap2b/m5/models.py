import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "database.db")

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database initialized.")

def get_user_by_username(username):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    return user

def get_all_mahasiswa():
    conn = get_db_connection()
    mahasiswa_list = conn.execute('SELECT * FROM mahasiswa ORDER BY nama').fetchall()
    conn.close()
    return mahasiswa_list

def get_mahasiswa_by_id(mahasiswa_id):
    conn = get_db_connection()
    mahasiswa = conn.execute('SELECT * FROM mahasiswa WHERE id = ?', (mahasiswa_id,)).fetchone()
    conn.close()
    return mahasiswa

def add_mahasiswa_db(nama, nim):
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO mahasiswa (nama, nim) VALUES (?, ?)', (nama, nim))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

def update_mahasiswa_db(mahasiswa_id, nama, nim):
    conn = get_db_connection()
    try:
        conn.execute('UPDATE mahasiswa SET nama = ?, nim = ? WHERE id = ?', (nama, nim, mahasiswa_id))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

def delete_mahasiswa_db(mahasiswa_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM mahasiswa WHERE id = ?', (mahasiswa_id,))
    conn.commit()
    conn.close()

def count_mahasiswa():
    conn = get_db_connection()
    count = conn.execute('SELECT COUNT(id) FROM mahasiswa').fetchone()[0]
    conn.close()
    return count

if not os.path.exists(DATABASE_URL):
    init_db()
else:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    if cursor.fetchone() is None:
        conn.close()
        init_db()
    else:
        conn.close()