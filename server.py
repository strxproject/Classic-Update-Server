from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/getchangelog', methods=['GET'])
def get_changelog():
    changelog_path = 'changelog.txt'

    if not os.path.exists(changelog_path):
        return Response("Changelog file not found.", status=404)
    
    with open(changelog_path, 'r') as file:
        changelog_content = file.read()
        
    return Response(changelog_content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
