from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_form, name="upload_form"),   # rota da página inicial do app
    path("stream/", views.stream_frame, name="stream_frame"),
]
