"""
WSGI config for cs50s90 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs50s90.settings')

application = get_wsgi_application()

# Code to help deploy with Heroku
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
