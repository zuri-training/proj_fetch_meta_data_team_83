web: python fetch_metadata/manage.py runserver 0.0.0.0:$PORT --settings=fetch_metadata.herokusettings
release: python fetch_metadata/manage.py migrate
release: python -m celery -A fetch_metadata worker
release: redis-server