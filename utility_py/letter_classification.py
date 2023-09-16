# import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as image_preprocessing
from PIL import Image, ImageOps
import numpy as np


class LetterClassification:
    def __init__(self, model_path="../models/model_weights.h5"):
        # model_path =
        self.model = load_model(model_path, compile=False)
        self.input_shape = (64, 64)
        self.class_labels = [
                        'ا',  'ب',  'ت',  'ث',  'ج',  'ح',  'خ',  # خ 6
                        'د',  'ذ',  'ر',  'ز',  'س',  'ش',  'ص',  # ص13
                        'ض',  'ط',  'ظ',  'ع',  'غ',  'ف',  'ق',  # ق 20
                        'ك',  'ل',  'م',  'ن',  'ه',  'و',  'ي',  # ي 27
                        'لا',  # لا  29
          ]

    def image_preprocessing(self, letter_image):
        """
        gray scaling
        normalization
        resizing

        :param letter_image: PIL image object
        :return: pre processed image
        """
        mode = letter_image.mode  # expecting "RGB" or "L" for gray
        if mode != "L ":
            # if not gray turn gray
            letter_image = ImageOps.grayscale(letter_image)

        # normalize and resize to input size
        letter_image = letter_image.resize( self.input_shape)
        letter_image = np.array(letter_image)
        letter_image = letter_image / 255
        letter_image = np.reshape(letter_image, (1, self.input_shape[0], self.input_shape[1], 1))
        return letter_image

    def classify_letter(self, letter_image):
        """

        :param letter_image: image containing only one letter(a white letter on a black background)
        :return: {letter, confidence score)
        """
        processed_letter_img = self.image_preprocessing(letter_image)
        prediction = self.model(processed_letter_img)
        index = np.argmax(prediction)
        confidence = prediction[0, index].numpy()
        result = (self. class_labels[index], confidence)
        return result


if __name__ == '__main__':
    # debugging
    classifier = LetterClassification()
    test_image = "../input/dataset/28_lamalif/3059.png"
    import base64

    with open(test_image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    from io import BytesIO
    import base64

    im = Image.open(BytesIO(base64.b64decode(encoded_string)))
    result = classifier.classify_letter(im)
    print(result)
