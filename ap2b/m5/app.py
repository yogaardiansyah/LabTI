from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from werkzeug.routing import Map, Rule
from dotenv import load_dotenv
import os
import models
from functools import wraps
import datetime
import sqlite3

load_dotenv()

app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv("SECRET_KEY", "defaultsecretkeyforflask")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.before_request
def before_request_func():
    g.year = datetime.date.today().year

def view_home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

def view_login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = models.get_user_by_username(username)
        if user and user['password'] == password:
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Login Gagal. Username atau password salah.", "danger")
    return render_template('login.html')

@login_required
def view_dashboard():
    total_mahasiswa = models.count_mahasiswa()
    return render_template('dashboard.html',
                           user=session['username'],
                           total_mahasiswa=total_mahasiswa)

@login_required
def view_logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@login_required
def view_mahasiswa_index():
    mahasiswa_data = models.get_all_mahasiswa()
    return render_template('mahasiswa/index.html', mahasiswa_list=mahasiswa_data)

@login_required
def view_add_mahasiswa():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        if not nama or not nim:
            flash("Nama dan NIM tidak boleh kosong.", "warning")
            return render_template('mahasiswa/add.html', mahasiswa={'nama': nama, 'nim': nim})
        if models.add_mahasiswa_db(nama, nim):
            flash(f"Mahasiswa '{nama}' berhasil ditambahkan.", "success")
            return redirect(url_for('mahasiswa_index'))
        else:
            flash(f"Gagal menambahkan mahasiswa. NIM '{nim}' mungkin sudah ada.", "danger")
            return render_template('mahasiswa/add.html', mahasiswa={'nama': nama, 'nim': nim})
    return render_template('mahasiswa/add.html', mahasiswa=None)

@login_required
def view_update_mahasiswa(mahasiswa_id):
    mhs = models.get_mahasiswa_by_id(mahasiswa_id)
    if not mhs:
        flash("Mahasiswa tidak ditemukan.", "danger")
        return redirect(url_for('mahasiswa_index'))
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        if not nama or not nim:
            flash("Nama dan NIM tidak boleh kosong.", "warning")
            return render_template('mahasiswa/update.html', mahasiswa={'id': mahasiswa_id, 'nama': nama, 'nim': nim})
        if models.update_mahasiswa_db(mahasiswa_id, nama, nim):
            flash(f"Mahasiswa '{nama}' berhasil diupdate.", "success")
            return redirect(url_for('mahasiswa_index'))
        else:
            flash(f"Gagal mengupdate mahasiswa. NIM '{nim}' mungkin sudah digunakan mahasiswa lain.", "danger")
            return render_template('mahasiswa/update.html', mahasiswa={'id': mahasiswa_id, 'nama': nama, 'nim': nim})
    return render_template('mahasiswa/update.html', mahasiswa=mhs)

@login_required
def view_delete_mahasiswa(mahasiswa_id):
    mhs = models.get_mahasiswa_by_id(mahasiswa_id)
    if not mhs:
        flash("Mahasiswa tidak ditemukan.", "danger")
        return redirect(url_for('mahasiswa_index'))
    if request.method == 'POST':
        models.delete_mahasiswa_db(mahasiswa_id)
        flash(f"Mahasiswa '{mhs['nama']}' berhasil dihapus.", "success")
        return redirect(url_for('mahasiswa_index'))
    return render_template('mahasiswa/delete.html', mahasiswa=mhs)

app.add_url_rule('/', endpoint='home', view_func=view_home)
app.add_url_rule('/login', endpoint='login', view_func=view_login, methods=['GET', 'POST'])
app.add_url_rule('/dashboard', endpoint='dashboard', view_func=view_dashboard)
app.add_url_rule('/logout', endpoint='logout', view_func=view_logout)
app.add_url_rule('/mahasiswa/', endpoint='mahasiswa_index', view_func=view_mahasiswa_index)
app.add_url_rule('/mahasiswa/add', endpoint='add_mahasiswa', view_func=view_add_mahasiswa, methods=['GET', 'POST'])
app.add_url_rule('/mahasiswa/delete/<int:mahasiswa_id>', endpoint='delete_mahasiswa', view_func=view_delete_mahasiswa, methods=['GET', 'POST'])
app.add_url_rule('/mahasiswa/update/<int:mahasiswa_id>', endpoint='update_mahasiswa', view_func=view_update_mahasiswa, methods=['GET', 'POST'])

if __name__ == '__main__':
    db_path = os.getenv("DATABASE_URL", "database.db")
    if not os.path.exists(db_path) or os.path.getsize(db_path) == 0:
        print(f"Database at '{db_path}' not found or empty, initializing...")
        models.init_db()
    else:
        conn = None
        try:
            conn = models.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM users LIMIT 1;")
            cursor.execute("SELECT 1 FROM mahasiswa LIMIT 1;")
        except sqlite3.OperationalError:
            print("Tables not found in database, re-initializing...")
            if conn: conn.close()
            models.init_db()
        finally:
            if conn: conn.close()

    app.run(debug=True)
