from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from .models import (
    Organization,
    UploadBatch,
    RawEmissionRecord,
)

import pandas as pd


@api_view(["POST"])
def upload_csv(request):

    csv_file = request.FILES.get("file")

    if not csv_file:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    df = pd.read_csv(csv_file)

    organization, created = Organization.objects.get_or_create(
    name="Demo Organization"
)

    batch = UploadBatch.objects.create(
        organization=organization,
        source_type="SAP",
        original_filename=csv_file.name,
        status="COMPLETED"
    )

    for _, row in df.iterrows():

        status = "PENDING"

        if row["value"] < 0:
            status = "FLAGGED"

        if row["value"] > 10000:
            status = "FLAGGED"

        if not row["unit"]:
            status = "FLAGGED"

        scope = "Scope 1"

        if "Electricity" in row["activity_type"]:
            scope = "Scope 2"

        if "Flight" in row["activity_type"]:
            scope = "Scope 3"

        RawEmissionRecord.objects.create(
            organization=organization,
            upload_batch=batch,
            activity_type=row["activity_type"],
            source_value=row["value"],
            source_unit=row["unit"],
            normalized_value=row["value"] * 2.5,
            activity_date=row["date"],
            status=status,
            scope_category=scope,
        )

    return Response({
        "message": "CSV uploaded successfully"
    })


def upload_page(request):
    return render(request, "upload.html")