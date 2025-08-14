from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render

@method_decorator(csrf_exempt, name='dispatch')
class ImageUploadView(View):
    def post(self, request, *args, **kwargs):
        if not request.FILES:
            return JsonResponse({'error': 'Nenhuma imagem enviada.'}, status=400)

        saved_files = []
        for file_key in request.FILES:
            image = request.FILES[file_key]
            path = default_storage.save(f'uploaded_images/{image.name}', image)
            saved_files.append(path)

        return JsonResponse({'message': 'Imagens recebidas com sucesso.', 'arquivos_salvos': saved_files})

def upload_form(request):
    return render(request, 'upload/upload_form.html')
