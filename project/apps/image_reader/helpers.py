import os
import base64
from io import BytesIO
from PIL import Image, ImageOps
from tempfile import NamedTemporaryFile
import numpy


def turn_image_into_28px_image(image_file):
    """
    Turns a full-size image of unknown dimensions into a 20x20 square,
    then surrounds it with 8px of white so the result is a 28x28 image.
    """
    orig = Image.open(image_file)
    image_20 = ImageOps.fit(orig, (20, 20), Image.ANTIALIAS, 0, (0.5, 0.5))
    image_28 = ImageOps.expand(image_20, border=4, fill='white')
    image_28_buffer = BytesIO()
    image_28.save(image_28_buffer, format="PNG", quality=100)
    image_28_buffer.seek(0)
    return image_28


def turn_small_image_into_array(small_image):
    """
    Takes a 28x28 image, and returns a 28x28 array of brightness values (0-1)
    """
    converted_image = small_image.convert("L")
    pixel_array = numpy.array(converted_image)
    inverted_array = []
    for row in pixel_array:
        inverted_row = []
        for col in row:
            inverted_row.append(255 - col)
        inverted_array.append(inverted_row)

    return numpy.array(inverted_array)


def image_as_base64(image_file, format='png'):
    image_buffer = BytesIO()
    image_file.save(image_buffer, format="PNG", quality=100)
    image_buffer.seek(0)
    encoded_string = base64.b64encode(image_buffer.read()).decode()
    return 'data:image/%s;base64,%s' % (format, encoded_string)
