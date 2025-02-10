from flask import Flask, send_from_directory, request, json, render_template
from flask_cors import CORS
import sys
import argparse
import os
import hashlib

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.path.abspath(directory)

def get_file_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

is_build = hasattr(sys, '_MEIPASS')
app = Flask(__name__, static_folder='public', template_folder='public')
CORS(app)

versionPath = create_directory_if_not_exists('versions')

@app.route("/api/versions")
def version():
    files = []
    for filename in os.listdir(versionPath):
        file_path = os.path.join(versionPath, filename)
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)
            if ext == '.exe':
                file_info = {
                    "name": name,
                    "size": os.path.getsize(file_path),
                    "md5": get_file_md5(file_path),
                    "url": f"{request.host_url}api/versions/download/{filename}"
                }
                files.append(file_info)

    return json.jsonify(files)

@app.route("/api/versions/download/<version>")
def download(version):
    if not os.path.exists(versionPath):
        print('VERSION_NOT_FOUND')
        return 'VERSION_NOT_FOUND', 404
    return send_from_directory(versionPath, version)

def generatedIndex():
    api_url = request.host_url
    if is_build:
        api_url = api_url.replace('http://', 'https://')
    return render_template('index.html', api_url=api_url)

@app.route('/')
def index():
    return generatedIndex()

@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('api'):
        return 'API'
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return generatedIndex()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5400, help='Port to run the server on')
    args = parser.parse_args()

    if is_build:
        from waitress import serve
        serve(app, host='0.0.0.0', port=args.port)
        print('Running in production mode')
        print(f'Listening on http://0.0.0.0:{args.port}')
    else:
        app.run(debug=True, port=args.port)