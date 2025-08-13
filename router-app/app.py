from flask import Flask, jsonify
import requests

app = Flask(__name__)

HELLO_APP_BASE_URL = "http://localhost:5001"

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello, I am just a router and testing webhook with sidecar | final test before release"})

@app.route('/route', methods=['GET'])
def route():
    try:
        response = requests.get(f"{HELLO_APP_BASE_URL}/hello")
        return jsonify({"router_response": response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/read-file', methods=['GET'])
def read_file():
    try:
        response = requests.get(f"{HELLO_APP_BASE_URL}/read-file")
        return jsonify({"file_content_from_hello_app": response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
