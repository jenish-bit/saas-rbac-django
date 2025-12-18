
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_rbac.settings.local')

app = Celery('saas_rbac')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()