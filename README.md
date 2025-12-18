# Multi-Tenant SaaS Role & Permission Management System
Production-Ready Django Backend with JWT, RBAC, Audit Logging & Docker

![Django](https://img.shields.io/badge/Django-5.0+-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14+-FF1709?logo=djangorestframework)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?logo=postgresql)
![Redis](https://img.shields.io/badge/Redis-7+-DC382D?logo=redis)
![Docker](https://img.shields.io/badge/Docker-24+-2496ED?logo=docker)

A secure, scalable backend for SaaS applications featuring organization-based role management, JWT authentication, and audit trails — built with industry best practices.

## Features

- Multi-Tenancy: Isolated workspaces (organizations) for different companies
- RBAC (Role-Based Access Control): Granular permissions (can_invite_user, can_manage_roles)
- JWT Authentication: Stateless token-based auth for modern frontends
- Audit Logging: Track all user actions for compliance
- Async Invitations: Celery + Redis for background email processing
- Docker Ready: One-command containerized deployment
- Swagger API Docs: Interactive OpenAPI documentation

## Tech Stack

| Layer          | Technologies                                                                 |
|----------------|------------------------------------------------------------------------------|
| Backend        | Python 3.11, Django 5, Django REST Framework                                 |
| Auth           | JWT (djangorestframework-simplejwt)                                          |
| Database       | PostgreSQL (production), SQLite (development)                                |
| Cache/Broker   | Redis (Celery broker + caching)                                              |
| API Docs       | drf-spectacular (OpenAPI 3.0)                                                |
| Deployment     | Docker, Gunicorn, Nginx (via Docker Compose)                                 |
| Testing        | pytest                                                                       |

## Quick Start

### Prerequisites
- Python 3.11+
- pip
- Git

### Run Locally
```bash
# Clone the repo
git clone https://github.com/jenish-bit/saas-rbac-django.git
cd saas-rbac-django

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser --email admin@example.com --name Admin

# Start server
python manage.py runserver
```

### Access Endpoints
- Admin Panel: http://127.0.0.1:8000/admin/
- API Docs: http://127.0.0.1:8000/api/docs/

## Project Structure
```
saas_rbac/
├── apps/                   # Modular apps (accounts, roles, etc.)
│   ├── accounts/           # Custom user model + auth
│   ├── organizations/      # Multi-tenant workspaces
│   ├── roles/              # RBAC system (roles, permissions, memberships)
│   ├── auditlogs/          # User activity tracking
│   ├── invitations/        # Async user invites (Celery)
│   └── common/             # Base models + utils
├── saas_rbac/              # Django config (split settings)
│   ├── settings/
│   │   ├── base.py         # Core settings
│   │   ├── local.py        # Development settings
│   │   └── production.py   # Production settings
│   └── ...
├── config/                 # Celery config
├── Dockerfile              # Production-ready container
├── docker-compose.yml      # Local dev environment (PostgreSQL + Redis)
└── requirements.txt        # Dependencies
```

## Security Practices
- JWT with refresh tokens (15m access / 7d refresh)
- RBAC middleware with Redis-cached permission checks
- Soft deletes for data integrity
- Environment-based settings (no secrets in code)
- Rate limiting ready (add django-ratelimit)

## Docker Deployment
```bash
docker-compose up --build
```
- PostgreSQL (port 5432)
- Redis (port 6379)
- Django (port 8000)

## Resume Highlight
Built a multi-tenant SaaS backend using Django & DRF featuring JWT authentication, organization-based RBAC, Redis caching, Celery background tasks, audit logging, and Dockerized deployment.

## License
MIT
