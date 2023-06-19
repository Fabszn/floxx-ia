from PIL.Image import Image
from flask import Flask, request, jsonify
from werkzeug.datastructures import FileStorage
from storage import storage
from ia.detector import runIA
from flask_cors import CORS, cross_origin

from configuration import config
from PIL import Image
from io import BytesIO

from storage.storage import Storage

appConfig = config.AppConfig('config.json')
storage: Storage = storage.StorageBuilder(appConfig).build()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route("/detect/<idslot>", methods=['POST'])
def photo(idslot:str):
    img = storage.readFile(idslot)
    if img == None :
        response = jsonify({'nbp': result})
        response.status = 400
        response.content_type = "application/json"

        return response


@app.route("/photo", methods=['POST'])
def photo():
    impage_posted: FileStorage = request.files["file"]

    image_stream = BytesIO(impage_posted.read())

    # Ouvrir l'image avec PIL
    image_pil: Image = Image.open(image_stream)
    # Save on Cellar Clevercloud FS

    storage.saveFile(image_pil, impage_posted.filename)
    result = runIA(image_pil)
    response = jsonify({'nbp': result})

    # Set the Access-Control-Allow-Origin header to allow requests from any domain
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
