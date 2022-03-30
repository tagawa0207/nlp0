from django.urls import path

from . import views

app_name = 'nlp0'
urlpatterns = [
    path('', views.index, name='index'),
]
