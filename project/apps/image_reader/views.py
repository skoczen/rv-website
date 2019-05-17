from annoying.decorators import render_to
from image_reader.helpers import turn_image_into_28px_image, turn_small_image_into_array
from ml_models.mnist import guess_number


@render_to("image_reader/home.html")
def home(request):
    if request.method == "POST" and "picture" in request.FILES:
        image = request.FILES
        print(image)
        small_image = turn_image_into_28px_image(image)
        pixel_values = turn_small_image_into_array(small_image)
        number = guess_number(pixel_values)

        return {
            "number": number,
            "small_image": small_image,
            "image": image,
        }
    return locals()
