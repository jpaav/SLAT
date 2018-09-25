import os

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_!ee!ucsm_as@+7m2hr*10uh#@1q866splt_y2%$5on*e4#kbm'

DEBUG = True

DATABASES['default'] = {
	'ENGINE': 'django.db.backends.sqlite3',
	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}

ALLOWED_HOSTS += ['.herokuapp.com', '127.0.0.1', '0.0.0.0']
