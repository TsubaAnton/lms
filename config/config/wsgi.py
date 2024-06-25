"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import eventlet
from django.core.wsgi import get_wsgi_application

# Патчим eventlet до импорта Django для корректной работы с асинхронными операциями
eventlet.monkey_patch()

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Получаем WSGI-приложение Django
application = get_wsgi_application()

