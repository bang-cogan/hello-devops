import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    msg = os.getenv("APP_MESSAGE", "Hello from CNAPP World!")
    return render_template('index.html', message=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Demo login logic (tidak sungguhan)
        if username == 'admin' and password == '1234':
            return render_template('index.html', message=f"Welcome, {username}!")
        else:
            return render_template('login.html', error="Invalid credentials. Try again.")

    return render_template('login.html')

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)