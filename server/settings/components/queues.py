"""
This module is used to setup celery and rabbitmq.

See docs:
- http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
- https://github.com/celery/django-celery-beat
- http://docs.celeryproject.org/en/latest/userguide/monitoring.html

"""

from server.settings.components import config

BROKER_URL = 'amqp://{login}:{password}@{host}:{port}'.format(
    login=config('RABBITMQ_DEFAULT_USER'),
    password=config('RABBITMQ_DEFAULT_PASS'),
    host=config('RABBITMQ_HOST'),
    port=config('RABBITMQ_PORT'),
)
CELERY_BROKER_URL = BROKER_URL

# Task serialization settings:
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_BROKER_CONNECTION_TIMEOUT = 10
CELERY_REDIS_SOCKET_CONNECT_TIMEOUT = 10
CELERY_TASK_IGNORE_RESULT = False
CELERY_TASK_RESULT_EXPIRES = 5  # mins

# Results:
CELERY_RESULT_BACKEND = 'django-db'

# Scheduler:
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
