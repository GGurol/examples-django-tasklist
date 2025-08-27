"""
Django settings for the django_tasklist project.
Modernized for Django 4.2 and Python 3.12 in a Docker environment.
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# --- Core Settings ---

# SECURITY WARNING: keep the secret key used in production secret!
# It's better to load this from an environment variable.
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-a-default-secret-key-for-development')

# SECURITY WARNING: don't run with debug turned on in production!
# The 'DEBUG' value is read from an environment variable, defaulting to True for development.
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Allow all hosts during development in Docker. For production, this should be more specific.
ALLOWED_HOSTS = ['*']


# --- Application Definition ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # For serving static files
    'django.contrib.staticfiles',
    'mc_tasklist',
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise middleware should be placed right after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # Re-enabled for security
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_tasklist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Add a project-level templates directory
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_tasklist.wsgi.application'


# --- Database Configuration ---

# This project was originally designed for PostgreSQL (based on requirements.txt).
# The configuration is read from the DATABASE_URL environment variable in docker-compose.yml.
# This makes the project database-agnostic.
#
# For local development with SQLite (if no DATABASE_URL is set):
default_db_url = 'sqlite:///' + str(BASE_DIR / 'db.sqlite3')

DATABASES = {
    'default': dj_database_url.config(default=default_db_url, conn_max_age=600)
}

# Auto-created primary key type (modern standard)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Password Validation ---

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- Internationalization ---

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- Static Files (CSS, JavaScript, Images) ---

STATIC_URL = '/static/'
# Directory where collectstatic will gather static files for production.
STATIC_ROOT = BASE_DIR / "staticfiles"
# Simplified static file serving with WhiteNoise.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Tell Django where to find our project-level static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# --- Caching & Sessions ---

# Simplified for development. For production, configure a real cache like Redis or Memcached.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"