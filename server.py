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

@app.route('/getchangelog', methods=['GET'])
def get_changelog():
    changelog_path = 'changelog.txt'

    app.logger.debug(f"Checking if {changelog_path} exists.")
    if not os.path.exists(changelog_path):
        app.logger.error("Changelog file not found.")
        return Response("Changelog file not found.", status=404)
    
    app.logger.debug(f"Reading {changelog_path}.")
    with open(changelog_path, 'r') as file:
        changelog_content = file.read()

    app.logger.debug("Reading version from version.txt.")
    version = read_version()
    if version is None:
        app.logger.error("Version information not found in version.txt.")
        return Response("Version information not found in version.txt.", status=400)

    response_data = {
        'changelog': changelog_content,
        'version': version
    }
    
    app.logger.debug("Returning response data.")
    return jsonify(response_data)

@app.route('/updates/<path:filename>', methods=['GET'])
def download_file(filename):
    updates_dir = 'updates'
    if '..' in filename:
        app.logger.error(f"Invalid file path detected: {filename}")
        return Response("Invalid file path.", status=400)
    return send_from_directory(updates_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
