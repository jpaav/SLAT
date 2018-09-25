import dj_database_url

from .base import *

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

SECRET_KEY = os.environ['SECRET_KEY']

if os.environ['DEBUG'].lower() in ['true', 't', 'y', 'yes']:
	DEBUG = True
else:
	DEBUG = False

ALLOWED_HOSTS += ['slat-backend.herokuapp.com']
