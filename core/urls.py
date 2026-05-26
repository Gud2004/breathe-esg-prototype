from django.contrib import admin
from django.urls import path

from ingestion.views import (
    upload_csv,
    upload_page,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('upload/', upload_csv),

    path('', upload_page),
]