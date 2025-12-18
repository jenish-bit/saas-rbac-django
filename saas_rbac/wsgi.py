import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Add 'apps/' to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / 'apps'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_rbac.settings.local')
application = get_wsgi_application()