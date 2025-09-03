from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('upload.urls')),      # raiz vai para app upload
    path("upload/", include("upload.urls")),
    path('cadastro/', include('cadastro.urls')),  # rota cadastro
]

# Servir arquivos estáticos de mídia em DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
