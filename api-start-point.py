from flask import Flask, request
# import model


# load model
app = Flask(__name__)
model_path = "./model/..."


@app.route('/classify_image')
def classify_image_char():
    """
    api function
    once hit with a 64 x 64 image containing a hand written letter
    classifies the letter as one of the 28 letters in the arabic alphabet


    :return: responds with the letter
    """
    app.logger.info(f'classification endpoint hit by ip {request.remote_addr}')
    app.logger.info("not yet complete")
    # preprocessing if needed
    # inference
    response =" will later be the letter of the alphabet  that was matched to the image "
    return response


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=105)
    app.logger.info(f'server up')
