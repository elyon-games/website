from flask import Flask, send_from_directory
import sys

is_build = hasattr(sys, '_MEIPASS')
app = Flask(__name__, static_folder='public')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('api'):
        return 'API'
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=not is_build)
