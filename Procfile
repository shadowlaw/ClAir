release: python flask-migrate.py db upgrade --directory migrations
web gunicorn -w 4 -b "0.0.0.0:$PORT" run:app
