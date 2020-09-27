#!/bin/bash
gunicorn_path=$(find /home/benchmark/.cache/pypoetry/virtualenvs -name "gunicorn" | grep -v lib)
${gunicorn_path} -b :8000 benchmark.wsgi
