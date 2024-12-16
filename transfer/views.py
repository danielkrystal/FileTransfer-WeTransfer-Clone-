from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse, Http404
from .models import FileTransfer
import uuid
from datetime import timedelta
from django.utils import timezone

# Upload view
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        expiry = timezone.now() + timedelta(days=7)
        transfer = FileTransfer.objects.create(
            uploaded_file=uploaded_file,
            download_link=str(uuid.uuid4()),
            expiry_date=expiry
        )
        return render(request, 'transfer/success.html', {'link': transfer.download_link})
    return render(request, 'transfer/upload.html')

# Download view
def download_file(request, link):
    try:
        transfer = FileTransfer.objects.get(download_link=link)
        if transfer.expiry_date < timezone.now():
            return HttpResponse("This link has expired.", status=410)
        response = HttpResponse(transfer.uploaded_file.open('rb'), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={transfer.uploaded_file.name}'
        return response
    except FileTransfer.DoesNotExist:
        raise Http404("File not found")
