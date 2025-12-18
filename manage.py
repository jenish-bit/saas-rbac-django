#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

if __name__ == '__main__':
    # Add 'apps/' to Python path BEFORE loading settings
    BASE_DIR = Path(__file__).resolve().parent
    sys.path.insert(0, str(BASE_DIR / 'apps'))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_rbac.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django..."
        ) from exc
    execute_from_command_line(sys.argv)