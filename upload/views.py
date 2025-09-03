from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.conf import settings
import datetime

@csrf_exempt
def stream_frame(request):
    if request.method == "POST" and request.FILES.get("frame"):
        frame = request.FILES["frame"]
        filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + ".jpg"
        path = os.path.join("uploaded_images", filename)
        saved_path = default_storage.save(path, ContentFile(frame.read()))
        return JsonResponse({"status": "ok", "file": saved_path})
    return JsonResponse({"status": "error"}, status=400)


from django.shortcuts import render

def upload_form(request):
    return render(request, "upload/upload_form.html")