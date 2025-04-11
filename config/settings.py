from pathlib import Path
from datetime import timedelta

from decouple import config
from corsheaders.defaults import default_headers


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

ADDITIONAL_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

OWN_APPS = [
    'src.accounts',
    'src.users',
    'src.rewards'
]

INSTALLED_APPS = DJANGO_APPS + ADDITIONAL_APPS + OWN_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2)
}

AUTH_USER_MODEL = 'accounts.User'

MIGRATION_MODULES = {
    'accounts': 'migrations.accounts_migrations',
    'rewards': 'migrations.rewards_migrations',
}


CELERY_RESULT_BACKEND = 'redis://' + config('REDIS_HOST') + ':' + config('REDIS_PORT') + '/0'
CELERY_BROKER_URL = 'redis://' + config('REDIS_HOST') + ':' + config('REDIS_PORT') + '/0'
CELERY_ACCEPT_CONTENT = ["json",'application/msgpack']
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_EXTENDED = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = default_headers + (
    "cache-control",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Credentials",
)
CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST').split(',')