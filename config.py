import os

CSRF_ENABLED = True
SECRET_KEY = os.environ.get('CSRF_SECRET_KEY', os.urandom(32))
