from flask import Flask, send_from_directory, request, json, render_template, jsonify
from flask_cors import CORS
import sys
import argparse
import os
import hashlib
from datetime import datetime
from google import genai

nameBot = "Elya"

def get_python_files(directory):
    py_files = []
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        py_files.append({"path": file_path, "content": content})
                    except Exception as e:
                        print(f"Erreur lors de l'ouverture du fichier {file_path}: {e}")
    except Exception as e:
        print(f"Erreur lors de la recherche de fichiers Python dans le répertoire {directory}: {e}")
    return py_files

def get_markdown_files(directory):
    md_files = []
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        md_files.append({"path": file_path, "content": content})
                    except Exception as e:
                        print(f"Erreur lors de l'ouverture du fichier {file_path}: {e}")
    except Exception as e:
        print(f"Erreur lors de la recherche de fichiers Markdown dans le répertoire {directory}: {e}")
    return md_files

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
codePath = create_directory_if_not_exists('code')
docsPath = create_directory_if_not_exists('docs')

filesPY = get_python_files(codePath)
filesMD = get_markdown_files(docsPath)

def ask_gemini(question, history):
    try:
        client = genai.Client(api_key="AIzaSyC09tC_fH_ZzTrvqFVjZFE5VAhU6z8b-Gw")
    except Exception as e:
        print(f"Erreur lors de l'initialisation du client Gemini: {e}")
        return "Erreur dans l'initialisation de l'IA."

    contextFile = "\n".join([f"File: {f['path']}\n{f['content']}" for f in filesPY])
    contextDoc = "\n".join([f"File: {f['path']}\n{f['content']}" for f in filesMD])
    contextHistory = "\n".join([f"Question: {h['question']}\nAnswer: {h['answer']}\nTime: {h['time']}" for h in history])
    
    prompt = f"""
        Tu es une intelligence artificielle nommée "{nameBot}", spécialisée dans la réponse aux questions sur le projet Elyon Tanks, développé par Nathan Van Uytvanck et Théophile Melerowic, deux lycéens en Première NSI au lycée. Ce projet a été réalisé dans le cadre du Trophée NSI.

        Liens utiles :
        - Site du projet : https://elyon.younity-mc.fr/
        - Dépôt GitHub : https://github.com/elyon-games/tanks

        Documentation disponible :
        {contextDoc}

        Fichiers du projet :
        {contextFile}

        ### Règles de réponse
        - Clarté et précision : Sois aussi clair et précis que possible dans tes réponses.
        - Fiabilité : Ne dis rien dont tu n’es pas sûr. Si tu ne sais pas, indique-le plutôt que de donner une réponse incorrecte.
        - Pertinence : Réponds uniquement aux questions liées au projet. Ne mentionne pas d’informations hors sujet.
        - Code source : Si un utilisateur demande du code, tu peux soit en extraire du projet, soit proposer un exemple adapté à la demande.
        - Confidentialité : Tu ne peux pas parler du fichier "common.process", qui appartient au Groupe Younity. Indique simplement qu'il ne provient pas du projet Elyon Tanks.
        - Respect des consignes :
        - Ne parle pas de sujets NSFW ou pouvant être mal interprétés.
        - Ne mentionne pas de personnes qui ne sont pas liées au projet.
        - Ne fais pas référence aux balises <question> et </question> dans tes réponses.

        ### Cas particuliers
        - Si l'utilisateur veut build le projet, réfère-toi au fichier build.md.
        - Si l'utilisateur demande le nombre de lignes de code, indique qu'il peut utiliser "./scripts/line.exe".
        - Si une question est ambiguë, demande des précisions sans mentionner les balises <question>.
        - Si tu ne comprends pas le fonctionnement d’un code, dis-le plutôt que de donner une explication incorrecte.

        ### Historique des questions
        {contextHistory}

        L'historique est trié par date pour assurer la continuité des réponses.
        Date et heure actuelles : {datetime.now().isoformat()} (uniquement pour ton contexte, ne la mentionne pas dans tes réponses).

        Question posée :
        <question>{question}</question>
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API Gemini: {e}")
        return "Erreur lors de la génération de la réponse."


def get_versions():
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
    return files

@app.route("/api/ai/ask", methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    hystory = data.get('history', [])
    if question == '':
        return 'MISSING_QUESTION', 400
    answer = ask_gemini(question, hystory)
    return jsonify({"answer": answer})

@app.route("/api/versions")
def version():
    return jsonify(get_versions())

@app.route("/api/versions/latest")
def latest_version():
    versions = get_versions()
    if len(versions) == 0:
        return 'NO_VERSIONS_FOUND', 404
    return jsonify(versions[-1])

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