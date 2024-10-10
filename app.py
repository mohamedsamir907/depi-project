from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the depi-project API!"

@app.route('/status')
def status():
    return jsonify({"status": "running", "code": 200})

@app.route('/data')
def data():
    return jsonify({"data": {"name": "Example", "type": "Test"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
