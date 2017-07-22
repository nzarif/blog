web: gunicorn blog.wsgi --log-file -
worker: python worker.py
worker: celery -A blog worker