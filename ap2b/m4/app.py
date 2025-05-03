from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.routing import Map, Rule
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "defaultsecret")

users = {
    "admin": "password123"
}

mahasiswa_list = []

url_map = Map([
    Rule('/', endpoint='home'),
    Rule('/login', endpoint='login'),
    Rule('/dashboard', endpoint='dashboard'),
    Rule('/logout', endpoint='logout'),
    
    Rule('/mahasiswa/', endpoint='mahasiswa_index'),
    Rule('/mahasiswa/add', endpoint='add_mahasiswa', methods=['GET', 'POST']),
    Rule('/mahasiswa/delete/<int:index>', endpoint='delete_mahasiswa', methods=['GET', 'POST']),
    Rule('/mahasiswa/update/<int:index>', endpoint='update_mahasiswa', methods=['GET', 'POST']),
])

@app.before_request
def before_request():
    app.url_map = url_map

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        return "Login Gagal. Coba lagi."

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        total_mahasiswa = len(mahasiswa_list)
        return render_template('dashboard.html', user=session['username'], total_mahasiswa=total_mahasiswa)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/mahasiswa/')
def mahasiswa_index():
    return render_template('mahasiswa/index.html', mahasiswa=mahasiswa_list)

@app.route('/mahasiswa/add', methods=['GET', 'POST'])
def add_mahasiswa():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        mahasiswa_list.append({'nama': nama, 'nim': nim})
        return redirect(url_for('mahasiswa_index'))
    return render_template('mahasiswa/add.html')

@app.route('/mahasiswa/delete/<int:index>', methods=['GET', 'POST'])
def delete_mahasiswa(index):
    if request.method == 'POST':
        mahasiswa_list.pop(index)
        return redirect(url_for('mahasiswa_index'))
    return render_template('mahasiswa/delete.html', mahasiswa=mahasiswa_list[index])

@app.route('/mahasiswa/update/<int:index>', methods=['GET', 'POST'])
def update_mahasiswa(index):
    if request.method == 'POST':
        mahasiswa_list[index]['nama'] = request.form['nama']
        mahasiswa_list[index]['nim'] = request.form['nim']
        return redirect(url_for('mahasiswa_index'))
    return render_template('mahasiswa/update.html', mahasiswa=mahasiswa_list[index])

if __name__ == '__main__':
    app.run(debug=True)

