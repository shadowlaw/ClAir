release: python flask-migrate.py db upgrade --directory migrations
release: python intialize_db.py
web gunicorn -w 4 -b "0.0.0.0:$PORT" app:app
