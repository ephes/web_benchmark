#!/bin/bash
uvicorn_path=$(find /home/benchmark/.cache/pypoetry/virtualenvs -name "uvicorn" | grep -v lib)
${uvicorn_path} --port 9000 --host 0.0.0.0 --workers 8 benchmark.asgi:application
