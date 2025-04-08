import os
from pathlib import Path

# === Base Directory ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Security ===
SECRET_KEY = 'django-insecure-w80+lhf!lmmq378uyu5t#s)x9*xpaaq$+)nl+w&*jj(ac1*z3m'
DEBUG = True
ALLOWED_HOSTS = ['*']  # Set domains/IPs in production

# === Installed Apps ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # your app
]

# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# === URL Configuration ===
ROOT_URLCONF = 'mpghome.urls'

# === Templates ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # React entry point template here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mpghome.context_processors.reactjs_assets_paths',  # required by CFE guide
            ],
        },
    },
]

# === WSGI Application ===
WSGI_APPLICATION = 'mpghome.wsgi.application'

# === Database ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === Password Validation ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === Internationalization ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === Static & Media Files ===
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# STATIC_ROOT = BASE_DIR / 'staticfiles'  # used for collectstatic (production)
# STATICFILES_BASE = BASE_DIR / 'assets'  # your React build goes here
STATICFILES_BASE = BASE_DIR / "staticfiles"
# Dev or Prod build from React/Vite
REACT_JS_BUILD_DIR = STATICFILES_BASE / 'frontend' / 'dev'
if not DEBUG:
    REACT_JS_BUILD_DIR = STATICFILES_BASE / 'frontend' / 'prod'

STATICFILES_DIRS = [
    STATICFILES_BASE,
]


MEDIA_ROOT = BASE_DIR / 'media'

# === Default Auto Field ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

