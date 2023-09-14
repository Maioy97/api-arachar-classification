from flask import Flask, request
import tensorflow as tf


# load model
app = Flask(__name__)
model_path = "./model/..."
# load model


@app.route('/classify_image', methods=['GET'])  # get
def classify_image_char():
    """
    api function
    once hit with a 64 x 64 image containing a hand written letter
    classifies the letter as one of the 28 letters in the arabic alphabet


    :return: responds with the letter
    """
    image = request.args.get('img')
    app.logger.info(f'classification endpoint hit by ip {request.remote_addr}')
    app.logger.info("not yet complete")
    # preprocessing if needed
    try:
        # inference on image
        # result_id, confidence = model(image)
        response = {"letter": '', "Probability": 0}
        # "will later be the letter of the alphabet  that was matched to the image and the confidence"
        code = 200

    except:
        code = 500  # place holder for errors to be added later
    return response, code


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=105)
    app.logger.info(f'server up')
