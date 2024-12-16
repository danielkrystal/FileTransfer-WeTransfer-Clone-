from django.urls import path
from . import views

app_name = 'transfer'

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('download/<str:link>/', views.download_file, name='download_file'),
]