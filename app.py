import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    msg = os.getenv("APP_MESSAGE", "Hello from DevOps Simulation!")
    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)