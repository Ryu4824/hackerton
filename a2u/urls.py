from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image/', views.image, name='image'),
    path('upload/', views.upload_file, name='upload_file'),

]
