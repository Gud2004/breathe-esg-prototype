from django.contrib import admin
from .models import (
    Organization,
    UploadBatch,
    RawEmissionRecord,
)


admin.site.register(Organization)
admin.site.register(UploadBatch)
admin.site.register(RawEmissionRecord)