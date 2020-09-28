#!/bin/bash
uvicorn_path=$(find /home/benchmark/.cache/pypoetry/virtualenvs -name "uvicorn" | grep -v lib)
${uvicorn_path} -b :9000 --workers 8 benchmark.asgi:application
