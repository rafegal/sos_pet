release: python manage.py migrate
release: echo $GOOGLE_CREDENTIALS > /app/google-credentials.json
web: gunicorn sos_pet.wsgi --log-file -