web: bin/start-stunnel gunicorn project.wsgi -b "0.0.0.0:$PORT" --workers=8
beat: bin/start-stunnel celery beat --app project
celery: bin/start-stunnel celery worker --beat -c 8 -Q celery --app project
