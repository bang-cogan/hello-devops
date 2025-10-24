import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    msg = os.getenv("APP_MESSAGE", "Hello from CNAPP World!")
    return render_template('index.html', message=msg)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)