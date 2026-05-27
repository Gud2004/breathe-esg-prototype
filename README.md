# Breathe ESG – ESG Data Ingestion & Analyst Review Prototype

A prototype ESG ingestion platform built for the Breathe ESG Tech Intern Assignment.

This project simulates how enterprise ESG data is collected, normalized, validated, and reviewed before audit sign-off. The focus of the implementation was on realistic backend ingestion workflows and handling messy operational data rather than building a heavily polished frontend.

---

# Live Deployment

### Deployed Application
https://breathe-esg-prototype-1-v8ek.onrender.com

### Admin Panel
https://breathe-esg-prototype-1-v8ek.onrender.com/admin

---

# GitHub Repository

https://github.com/Gud2004/breathe-esg-prototype

---

# Project Overview

Enterprise ESG reporting is difficult because data does not come from a single clean system.

Different departments export data in different formats:
- SAP exports for procurement and fuel
- Utility portal exports for electricity usage
- Corporate travel platforms for flights and travel activity
- Manual spreadsheets maintained by sustainability teams

This prototype attempts to simulate that reality.

The system allows ingestion of ESG activity records, normalizes them into a common structure, categorizes them into Scope 1/2/3 emissions, flags suspicious values, and surfaces records for analyst review.

---

# Key Features

## ESG Data Ingestion

Supports ingestion of:
- SAP-style fuel/procurement exports
- Utility electricity records
- Corporate travel activity data

CSV uploads are supported through the web interface.

---

## Scope 1 / 2 / 3 Categorization

The ingestion pipeline automatically categorizes records into:
- Scope 1
- Scope 2
- Scope 3

based on activity type.

Example:
- Fuel combustion → Scope 1
- Electricity usage → Scope 2
- Flights/travel → Scope 3

---

## Validation & Anomaly Detection

The system flags suspicious or invalid rows automatically.

Implemented checks include:
- Negative values
- Extremely large values
- Missing units

Flagged records are stored with review status indicators.

---

## Analyst Review Workflow

Uploaded records are reviewable through Django Admin.

Analysts can:
- inspect uploaded rows
- review flagged records
- verify normalized values
- validate categorization
- audit uploaded batches

---

## Audit-Oriented Data Modeling

The database structure was designed around audit traceability.

The system tracks:
- source upload batch
- original filename
- organization ownership
- normalization status
- ingestion timestamps
- review state

---

# Tech Stack

## Backend
- Django
- Django REST Framework

## Data Processing
- Pandas

## Database
- SQLite

## Deployment
- Render

---

# Data Model

## Organization
Represents a client company whose ESG data is being onboarded.

---

## UploadBatch
Tracks ingestion sessions and uploaded files.

Stores:
- source type
- upload status
- original filename
- timestamps

---

## RawEmissionRecord
Stores normalized activity records.

Includes:
- activity type
- source value
- source unit
- normalized value
- activity date
- scope category
- review status

---

# Real-World Research & Assumptions

## SAP Fuel / Procurement Data

The prototype assumes flat-file CSV exports inspired by simplified SAP-style procurement/fuel exports.

Handled realities:
- inconsistent units
- irregular formatting
- inconsistent activity naming
- large numeric inconsistencies

---

## Utility Electricity Data

Modeled after utility portal CSV exports used by facilities teams.

Handled:
- electricity usage values
- billing-style consumption records
- unit normalization assumptions

---

## Corporate Travel Data

Modeled using simplified travel platform exports inspired by platforms like Concur/Navan.

Handled:
- flights
- travel activity categorization
- Scope 3 classification

---

# Design Priorities

The assignment emphasized realistic ESG ingestion behavior more than frontend polish.

Because of that, the project prioritizes:
- ingestion reliability
- normalization logic
- auditability
- realistic backend workflows
- explainable data modeling

instead of focusing heavily on UI complexity.

---

# Tradeoffs & Deliberate Simplifications

The following were intentionally simplified for assignment scope:

- No production-grade emission factor engine
- No OCR/PDF utility bill extraction
- No asynchronous ingestion queues
- No multi-step analyst approval workflow
- No React dashboard implementation
- No enterprise authentication layer

The goal was to keep the implementation focused, understandable, and defendable.

---

# Running Locally

## Clone Repository

```bash
git clone https://github.com/Gud2004/breathe-esg-prototype
```

---

## Navigate to Backend

```bash
cd backend
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Start Server

```bash
python manage.py runserver
```

---

# Repository Structure

```text
backend/
│
├── core/
├── ingestion/
├── templates/
├── requirements.txt
├── runtime.txt
└── manage.py
```

---

# Submission Notes

This project was built to demonstrate:
- backend system design
- ESG ingestion understanding
- handling of messy enterprise data
- audit-oriented workflows
- practical engineering tradeoffs

rather than simply building a generic CRUD application.

The implementation intentionally focuses more on realistic ingestion architecture and review workflows than visual polish.