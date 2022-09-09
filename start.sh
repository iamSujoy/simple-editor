!#/bin/bash
gunicorn -w 3 --bind 127.0.0.1:5000 wsgi:app