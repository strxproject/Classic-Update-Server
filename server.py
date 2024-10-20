from flask import Flask, Response, jsonify, send_from_directory
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def read_version():
    version_file_path = 'version.txt'
    if os.path.exists(version_file_path):
        with open(version_file_path, 'r') as version_file:
            return version_file.read().strip()
    return None

@app.route('/getversion', methods=['GET'])
def get_version():
    version = read_version()
    if version:
        return jsonify({'version': version})
    else:
        app.logger.error("Version file not found.")
        return Response("Version file not found.", status=404)

@app.route('/updates/<path:filename>', methods=['GET'])
def download_file(filename):
    updates_dir = 'updates'
    if '..' in filename:
        app.logger.error(f"Invalid file path detected: {filename}")
        return Response("Invalid file path.", status=400)
    return send_from_directory(updates_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
