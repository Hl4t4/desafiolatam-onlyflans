
python manage.py migrate

gunicorn onlyflans.wsgi --bind=0.0.0.0:80 