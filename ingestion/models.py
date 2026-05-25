from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UploadBatch(models.Model):
    SOURCE_CHOICES = [
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    original_filename = models.CharField(max_length=255)

    status = models.CharField(
        max_length=50,
        default="PENDING"
    )

    def __str__(self):
        return f"{self.organization.name} - {self.source_type}"


class RawEmissionRecord(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("FLAGGED", "FLAGGED"),
        ("APPROVED", "APPROVED"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    upload_batch = models.ForeignKey(
        UploadBatch,
        on_delete=models.CASCADE
    )

    activity_type = models.CharField(max_length=100)

    source_value = models.FloatField()

    source_unit = models.CharField(max_length=50)

    normalized_value = models.FloatField(
        null=True,
        blank=True
    )

    normalized_unit = models.CharField(
        max_length=50,
        default="kgCO2e"
    )

    activity_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.source_value}"