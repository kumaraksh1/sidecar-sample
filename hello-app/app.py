from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Hello App!, testing sidecar gha | final test before release"})


@app.route('/read-file', methods=['GET'])
def read_file():
    file_path = "/mnt/data/sample.txt"

    if not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return jsonify({"file_content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
