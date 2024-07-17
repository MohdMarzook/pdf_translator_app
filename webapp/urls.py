from django.urls import path
from .views import download_file, file_upload_view, index

urlpatterns = [
    path('', index, name='index'),
    path('upload/', file_upload_view, name='file_upload'),
    path('download/<uuid:unique_tag>/', download_file, name='pdf_download'),
]