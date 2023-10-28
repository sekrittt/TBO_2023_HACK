# flask --app serv run

import os
import json

from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename


def run(host, port, process_image):
    CURRENT_DIR = os.getcwd()

    UPLOAD_FOLDER = os.path.join(CURRENT_DIR, 'imgs')
    ALLOWED_EXTENSIONS = {'png'}

    app = Flask(__name__)
    home_file = ''
    with open(os.path.join(CURRENT_DIR, 'backend', 'ui', 'index.html'), 'r', encoding="utf-8") as f:
        home_file = f.read()

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    def process(filename: str) -> str:
        # Get sizes of image
        return json.dumps({"success": True, "message": "Upload!"})

    @app.route('/', methods=['POST'])
    def upload_file():
        # нет нет нет, не можем, у нас это должно всегда возвращать что-то
        if request.method == 'POST':
            file = request.files['file']
            if file and (file.content_type.rsplit('/', 1)[1] in ALLOWED_EXTENSIONS).__bool__():
                if file.filename is not None:
                    filename = secure_filename(file.filename)  # type: ignore

                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                    result = process(filename)
                    return result
        return json.dumps({
            "success": False,
            "message": "Error!"
        })

    @app.route('/', methods=['GET'])
    def home():
        return home_file

    @app.route('/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   filename)

    app.run(host=host, port=port)
