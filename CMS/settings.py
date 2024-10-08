

import os
import posixpath
import environ


env = environ.Env()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = "o!ld8nrt4vc*h1zoey*wj48x*q0#ss12h=+zh)kk^6b3aygg=!"


DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "accounts.User"


DJANGO_APPS = [
  
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
   
]

# Thired party apps
THIRED_PARTY_APPS = [
    "crispy_forms",
    "rest_framework",
]

# Custom apps
PROJECT_APPS = [
    "app.apps.AppConfig",
    "accounts.apps.AccountsConfig",
    "course.apps.CourseConfig",
    "result.apps.ResultConfig",
    "search.apps.SearchConfig",
    "quiz.apps.QuizConfig",
    "payments.apps.PaymentsConfig",
    "fees.apps.FeesConfig",
    "communication.apps.CommunicationConfig",
   
    
    
]

#'192.168.1.67'


# Combine all apps
INSTALLED_APPS = DJANGO_APPS + THIRED_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "CMS.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
            ],
        },
    },
]

WSGI_APPLICATION = "CMS.wsgi.application"

ASGI_APPLICATION = "CMS.asgi.application"


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# -----------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization


LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)


STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ["staticfiles"]))

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# -----------------------------------
# E-mail configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = (
    "smtp.gmail.com"  # Here i'm using gmail as the email host, but you can change it
)
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("USER_EMAIL")
EMAIL_HOST_PASSWORD = env("USER_PASSWORD")

# crispy config
CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# DRF setup
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

# Strip payment config
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")
