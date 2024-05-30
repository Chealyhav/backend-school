
from pathlib import Path
import os
import dj_database_url
import environ
env = environ.Env()
environ.Env.read_env()
CORS_ORIGIN_ALLOW_ALL = True


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY = 'pp#hk$6^0-1r1z*l-+_5$4&84#l482(fjf8#vn99x!1fax@0ik'
DEBUG = True
APPEND_SLASH = False
ALLOWED_HOSTS = ['*']
# Retrieve the DATABASE_URL environment variable
database_url = os.environ.get('DATABASE_URL')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'collection', 
    'drf_yasg',
    'admin_api',
    'rest_framework',
    'corsheaders',
    'schoolmanagement',
    'rest_framework.authtoken',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # Other authentication classes if needed
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

]

ROOT_URLCONF = 'schoolmanagement.urls'

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


WSGI_APPLICATION = 'schoolmanagement.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.mysql',
#     #     'NAME': 'dbschool',
#     #     'USER': 'root',
#     #     'PASSWORD':'',
#     #     'HOST': 'localhost',
#     #     'PORT': '3306', 
#     #       'OPTIONS': {
#     #         'charset': 'utf8mb4',
#     #         'init_command': "SET collation_connection = utf8mb4_unicode_ci"
              
#     #     },
#     # }
# }

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
        'default': dj_database_url.parse(database_url)
    }


AUTH_USER_MODEL = 'collection.User'
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# because in this we need to store media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'media'),
)