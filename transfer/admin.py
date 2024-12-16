from django.contrib import admin

# Register your models here.

# admin.py in transfer app
from django.contrib import admin
from .models import FileTransfer

@admin.register(FileTransfer)
class FileTransferAdmin(admin.ModelAdmin):
    list_display = ('uploaded_file', 'download_link', 'expiry_date')
