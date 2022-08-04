# """
# Django settings for fetch_metadata project.

# Generated by 'django-admin startproject' using Django 4.0.6.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.0/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.0/ref/settings/
# """
# import os
# from pathlib import Path
# from decouple import config


# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("DJANGO_SECRET_KEY",'django-insecure-j#$&w%&4m(rj!#dvzt3f3my#)qs)y5p)$x+3$sb^8@fp8858h&')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config("DJANGO_DEBUG",True)

# ALLOWED_HOSTS = []


# # Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

     # 3rd Party
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    # 'crispy_forms',

    #local apps
    'api.apps.ApiConfig',
    'apps.accounts',
    'apps.meta_extract.apps.MetaExtractConfig',
    'apps.commons.apps.CommonsConfig',
    'apps.file_control.apps.FileControlConfig',
]

AUTH_USER_MODEL = 'accounts.CustomUser'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'fetch_metadata.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             BASE_DIR/"templates",
#         ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'fetch_metadata.wsgi.application'



# #decouple database variables from .env
# PG_DB = config("PG_DB")
# PG_USER = config("PG_USER")
# PG_PASSWORD = config("PG_PASSWORD")
# PG_HOST = config("PG_HOST")
# PG_PORT = config("PG_PORT")

# # Database
# # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': PG_DB,
#         'USER': PG_USER,
#         'PASSWORD': PG_PASSWORD,
#         'HOST': PG_HOST,
#         'PORT': PG_PORT,
#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/4.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True

# #Media files (uploaded files)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = '/static/'
# if DEBUG:
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static')
#         ]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# #setup media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# #### REST_FRAME_WORK_SETTINGS#####
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#         # 'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES':[
#                 'rest_framework.permissions.IsAuthenticated',
#     ],
# }




"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#s8v!f!mcf8&7t_6@khus14(3yu@e#dkkvm35v1t)@89c08)!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"


# Application definition

# INSTALLED_APPS = [
#     'blog.apps.BlogConfig',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'tailwind',
#     'theme',
#     'django_browser_reload',
#     'users',
#     'crispy_forms',
# ]


INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fetch_metadata.urls'

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
# WSGI_APPLICATION = 'fetch_metadata.wsgi.application'
ASGI_APPLICATION = 'fetch_metadata.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
        ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# LOGIN_REDIRECT_URL =    'blog-home'

# LOGIN_URL =    'login'
