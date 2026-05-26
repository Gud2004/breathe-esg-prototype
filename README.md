# Breathe ESG Prototype

A Django-based ESG ingestion and review system prototype built for the Breathe ESG Tech Intern Assignment.

## Features

- CSV ingestion pipeline
- Multi-source ESG data support
    - SAP fuel/procurement exports
    - Utility electricity data
    - Corporate travel data
- Validation and suspicious row detection
- Scope 1 / Scope 2 / Scope 3 categorization
- Upload batch tracking
- Analyst review workflow using Django Admin
- Record filtering and search
- Unit normalization support
- Audit-friendly ingestion architecture

---

## Tech Stack

- Django
- Django REST Framework
- SQLite
- Pandas
- Python

---

## ESG Data Sources Modeled

### 1. SAP Fuel Data
Modeled as flat-file CSV exports with:
- plant codes
- fuel types
- units
- posting dates

### 2. Utility Electricity Data
Modeled as portal CSV exports with:
- meter IDs
- billing periods
- tariffs
- kWh usage

### 3. Corporate Travel Data
Modeled using:
- airport codes
- trip categories
- travel distance

---

## Validation Logic

The system automatically flags suspicious records:

- Negative values
- Extremely high usage values
- Missing units

Flagged records are surfaced for analyst review.

---

## Scope Categorization

| Activity Type | ESG Scope |
|---|---|
| Fuel | Scope 1 |
| Electricity | Scope 2 |
| Travel | Scope 3 |

---

## Running Locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Sample Files

- sample_sap_fuel.csv
- sample_utility_data.csv
- sample_travel_data.csv

---

## Admin Access

Django admin is used as the analyst review dashboard.

```text
/admin
```

---

## Future Improvements

- React dashboard
- PDF utility bill ingestion
- Authentication and role management
- AI anomaly detection
- Automated emission factor mapping
