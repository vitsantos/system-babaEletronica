from django.urls import path
from .views import ImageUploadView, upload_form

urlpatterns = [
    path('', upload_form, name='upload_form'),  # mostra o formulário
    path('upload/', ImageUploadView.as_view(), name='image_upload'),  # recebe o POST com as imagens
]


