#!/bin/bash
source /opt/venv/bin/activate

exec /opt/venv/bin/gunicorn -b 0.0.0.0:5001 wsgi:app