# flask --app serv run

import os
import json

from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename

from PIL import Image
from ultralytics.engine.results import Results
from collections import Counter


def run(host, port, process_image):
    CURRENT_DIR = os.getcwd()

    UPLOAD_FOLDER = os.path.join(CURRENT_DIR, 'imgs')
    ALLOWED_EXTENSIONS = {'png'}

    classes = ["wood", "glass", "plastic", "metal"]

    app = Flask(__name__)
    home_file = ''
    with open(os.path.join(CURRENT_DIR, 'backend', 'ui', 'index.html'), 'r', encoding="utf-8") as f:
        home_file = f.read()

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    def process(path: str, filename: str) -> str:
        # Get sizes of image
        image = Image.open(os.path.join(path, filename))
        res: list[Results] = process_image(image)
        print(Counter([classes[int(i)] for i in res[0].boxes.cls]))
        return json.dumps({"success": True, "message": "Upload!", "image_url": f'/predict/{filename}'})

    @app.route('/', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['file']
            if file and (file.content_type.rsplit('/', 1)[1] in ALLOWED_EXTENSIONS).__bool__():
                if file.filename is not None:
                    filename = secure_filename(file.filename)  # type: ignore

                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                    result = process(UPLOAD_FOLDER, filename)
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
    
    
    @app.route('/predict/<path:filename>')
    def uploaded_file1(filename):
        return send_from_directory(os.path.join(CURRENT_DIR, 'ai', 'predict'),
                                   filename)

    app.run(host=host, port=port, debug=True)
