release: python manage.py migrate --no-input --settings=SLAT.settings.production
web: gunicorn SLAT.wsgi --log-file -
