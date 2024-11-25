import os
from celery import Celery
# from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.setting.settings')

# Redis_Host = config("REDISHOST")

app = Celery('config', backend='redis', broker="redis://localhost:6379")

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Исправление для предупреждения
app.conf.broker_connection_retry_on_startup = True
app.conf.task_always_eager = True
