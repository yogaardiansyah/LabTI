from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "defaultsecret")

users = {
    "admin": "password123"
}

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
        return render_template('dashboard.html', user=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
