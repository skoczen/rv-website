from annoying.decorators import render_to
from image_reader.helpers import turn_image_into_28px_image, turn_small_image_into_array, image_as_base64
from ml_models.mnist import guess_number


@render_to("image_reader/home.html")
def home(request):
    submitted = False
    if request.method == "POST" and "picture" in request.FILES:
        submitted = True
        image = request.FILES["picture"]
        small_image = turn_image_into_28px_image(image)
        pixel_array = turn_small_image_into_array(small_image)
        number = guess_number(pixel_array)
        small_image_base64 = image_as_base64(small_image)

        return {
            "submitted": submitted,
            "number": number,
            "small_image": small_image,
            "pixel_array": pixel_array,
            "small_image_base64": small_image_base64,
            "image": image,
        }

    return {
        "submitted": submitted,
    }
