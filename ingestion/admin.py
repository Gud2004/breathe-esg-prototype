from django.contrib import admin

from .models import (
    Organization,
    UploadBatch,
    RawEmissionRecord,
)


@admin.register(RawEmissionRecord)
class RawEmissionRecordAdmin(admin.ModelAdmin):

    list_display = (
        "activity_type",
        "source_value",
        "source_unit",
        "status",
        "scope_category",
        "activity_date",
    )

    list_filter = (
        "status",
        "scope_category",
    )

    search_fields = (
        "activity_type",
    )


@admin.register(UploadBatch)
class UploadBatchAdmin(admin.ModelAdmin):

    list_display = (
        "organization",
        "source_type",
        "status",
        "uploaded_at",
    )

    list_filter = (
        "source_type",
        "status",
    )


admin.site.register(Organization)