# SaaS RBAC Project
# Multi-Tenant SaaS Role & Permission System

A production-ready Django backend for SaaS applications with:
- JWT Authentication
- Organization-based RBAC
- Audit Logging
- Celery + Redis
- Docker Support
- Swagger API Docs

## Run Locally
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver