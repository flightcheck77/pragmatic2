from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Take environment variables from .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['158.247.199.183']
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'fc12##fc34',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
