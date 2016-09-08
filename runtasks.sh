#!/bin/bash

# Run Celery tasks
PYTHONPATH=./ celery -A tasks worker --loglevel=debug
