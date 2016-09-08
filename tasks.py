# -*- coding: utf-8 -*-
# from celery_start import app
# from celery import Celery
#
# app = Celery('tasks', backend='amqp', broker='amqp://localhost')
from celery_start import app


@app.task
def add(x, y):
    return x + y
