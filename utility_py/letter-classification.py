# import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as image_preprocessing
from PIL import Image, ImageOps


class LetterClassification:
    def __init__(self):
        model_path = "./models/model_weights.h5"
        model = load_model(model_path)
        self.input_shape = (64, 64)
        class_labels = [
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

        :param letter_image:
        :return: pre processed image
        """
        # pillow image for the rest of the functions
        letter_image = Image.fromarray(letter_image)
        mode = letter_image.mode()  # expecting "RGB" or "L" for gray

        if mode != "L ":
            # if not gray turn gray
            letter_image = ImageOps.grayscale(letter_image)
        # normalize and resize to input size
        letter_image = letter_image/255
        letter_image = letter_image.resize(letter_image, self.input_shape)
        return letter_image

    def classify_letter(self, letter_image):
        """

        :param letter_image: image containing only one letter(a white letter on a black background)
        :return: {letter, confidence score)
        """
        processed_letter_img = self.image_preprocessing(letter_image)
        prediction = self.model(processed_letter_img)
        result = {"letter": self. class_labels[prediction[0]], "conf": prediction[1] }
        return result



if __name__ == '__main__':
    # debugging
    classifier = LetterClassification()
    test_image = "./input/data/0_alif/0.png"
    # import