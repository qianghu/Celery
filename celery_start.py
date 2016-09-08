# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('tasks')


class Config:
    BROKER_URL = 'amqp://localhost'
    CELERY_RESULT_BACKEND = 'amqp://'

    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json', 'pickle']
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_ENABLE_UTC = True

    CELERY_ROUTES = {
        'tasks.add': 'low-priority',
    }

app.config_from_object(Config)
