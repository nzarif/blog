web: gunicorn blog.wsgi --log-file -
worker: python worker.py
worker: celery -A WebProjectPhase3 worker