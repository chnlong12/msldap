"""
Django settings for adtest project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'he$op^k+w4&+j=ir@h7v#@p%g3=e$t$252=wct)2!is+ec9hq3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# start settings for ldap3 AD

# LDAP_SERVERS = [
#     {
#         'host': 'raykuan.com',
#         'port': 636,
#         'use_ssl': True,
#     },
#     {
#         'host': 'raykuan.com',
#         'port': 636,
#         'use_ssl': True,
#     },
# ]
#
# LDAP_ENGINE = 'AD'
# LDAP_BIND_USER = "cn=ldap,ou=others,ou=eptok,dc=raykuan,dc=com"
# LDAP_BIND_PASSWORD = "6yhnMJU&"
# LDAP_SEARCH_BASE = "dc=raykuan,dc=com"
# # LDAP_USER_SEARCH_FILTER = "(&(sAMAccountName=%s)(objectClass=user))"
# LDAP_USER_SEARCH_FILTER = "(&(|(userPrincipalName={0})(sAMAccountName={0}))(objectClass=user))"
#
# LDAP_ATTRIBUTES_MAP = {
#     'username': 'sAMAccountName',
#     'first_name': 'givenName',
#     'last_name': 'sn',
#     'email': 'mail',
# }
#
# LDAP_BIND_ADMIN = "cn=adsync,ou=others,ou=eptok,dc=raykuan,dc=com"
# LDAP_BIND_ADMIN_PASS = "6yhnMJU"
# LDAP_AD_DOMAIN = "raykuan.com"
# LDAP_CERT_FILE = "/raykuan/workspace/ldap_rync/certnew.pem"
#
#
# LDAP_USER_MODEL_USERNAME_FIELD = 'email' #default is username
# LDAP_USE_LDAP_GROUPS = True
# LDAP_GROUPS_SEARCH_BASE = "dc=raykuan,dc=com"
# LDAP_GROUPS_SEARCH_FILTER = "(&(objectClass=group))"
# LDAP_GROUP_MEMBER_ATTRIBUTE = "member"
# LDAP_SUPERUSER_GROUPS = ["CN=admin,dc=raykuan,dc=com", ]
# LDAP_STAFF_GROUPS = ["CN=staff,dc=raykuan,dc=com", ]
# LDAP_GROUPS_MAP = {
#     'my django group': "cn=my ldap group,dc=raykuan,dc=com",
# }
#
# AUTHENTICATION_BACKENDS = ("django_auth_ldap3_ad.auth.LDAP3ADBackend",)
#

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usermgt',
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

ROOT_URLCONF = 'adtest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'adtest.wsgi.application'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1200

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]