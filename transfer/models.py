import uuid

from django.db import models
from django.utils import timezone


# Create your models here.

class FileTransfer(models.Model):
    uploaded_file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    download_link = models.CharField(max_length=255, unique=True, blank=True)
    expiry_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.download_link:
            self.download_link = str(uuid.uuid4())  # Generate unique link
        if not self.expiry_date:
            self.expiry_date = timezone.now() + timezone.timedelta(days=7)  # 7-day expiry
        super().save(*args, **kwargs)