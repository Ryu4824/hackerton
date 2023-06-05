from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .test_image import load_image, test

def dict_to_class(dictionary, class_name):
    custom_class = type(class_name, (), dictionary)
    return custom_class

def index(request):
    context = {
        'static_url': settings.STATIC_URL,
    }
    return render(request, 'base.html', context)

def image(request):
    args = {
        "checkpoint" : './weights/face_paint_512_v2.pt',
        "input_dir" : './static/samples/inputs',
        "output_dir" : './static/samples/results',
        "device" : 'cpu',
        "x32" : True,
        "upsample_align" : False,
    }
    test(dict_to_class(args, "args"))
    return HttpResponse("Image Complete")

