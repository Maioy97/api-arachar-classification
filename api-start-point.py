from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
# import tensorflow as tf
from PIL import Image, ImageOps
from io import BytesIO
import base64
from utility_py.letter_classification import LetterClassification

app = Flask(__name__)
api = Api(app)
CORS(app)

# load model by initialising class
classifier = LetterClassification("./models/model_weights.h5")


class APICharacterClassification(Resource):

    def post(self):
        """
        api function
        once hit with a 64 x 64 image containing a hand written letter
        classifies the letter as one of the 28 letters in the arabic alphabet

        :return: responds with the letter
        """
        print(request)
        app.logger.debug(f' form {request.form}')
        app.logger.debug(f' files {request.files}')
        app.logger.debug(f' args {request.args}')
        encoded_string_img = request.form['img']
        im = Image.open(BytesIO(base64.b64decode(encoded_string_img)))
        app.logger.info(f'classification endpoint hit by ip {request.remote_addr}')
        try:
            # inference on image
            class_label, score = classifier.classify_letter(im)
            app.logger.debug(f' returned label {class_label}')
            response = {"letter": class_label, "Probability": score}
            app.logger.debug(f' returned response {response}')
            code = 200
            return response, code

        except Exception as e:
            code = 500  # place holder for errors to be added later
            response = {"message": f"error running model: {e}"}
            return response, code


class ApiWelcomeMessage(Resource):
    def get(self):
        return {
            "message": "Welcome to Mai's letter classification api",
            "parameters": "img : image sent in base64",
            "endpoint": "/classify-letter",
            }


api.add_resource(ApiWelcomeMessage, '/')
api.add_resource(APICharacterClassification, '/classify-letter')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8080)
    app.logger.info(f'server up')
