import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_project.settings')

app = Celery('crypto_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'fetch-crypto-prices-every-5-minutes': {
        'task': 'core.tasks.fetch_crypto_prices',
        'schedule': crontab(minute='*/5'),
    },
}
app.autodiscover_tasks() 



