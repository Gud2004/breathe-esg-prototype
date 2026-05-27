from django.urls import path
from .views import upload_csv, upload_page

urlpatterns = [
    path("upload/", upload_csv),
    path("upload-page/", upload_page),
]