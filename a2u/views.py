from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .test_image import load_image, test
from django.core.files.storage import default_storage

def dict_to_class(dictionary, class_name):
    custom_class = type(class_name, (), dictionary)
    return custom_class

def index(request):
    context = {
        'static_url': settings.STATIC_URL,
    }
    return render(request, 'base.html', context)

def image(request):
    file_name = request.FILES['name']
    input_dir = './static/samples/inputs/'
    file_path = default_storage.save(input_dir + file_name.name, file_name)
    args = {
        "checkpoint" : './weights/face_paint_512_v2.pt',
        "img_name" : file_name,
        "input_dir" : input_dir,
        "output_dir" : './static/samples/results/',
        "device" : 'cpu',
        "x32" : True,
        "upsample_align" : False,
    }
    test(dict_to_class(args, "args"))
    return HttpResponse("Image Complete")

