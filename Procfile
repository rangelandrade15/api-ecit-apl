release: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn escola_api.wsgi:application
