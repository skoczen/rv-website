from annoying.decorators import render_to


@render_to("website/home.html")
def home(request):
    return locals()
