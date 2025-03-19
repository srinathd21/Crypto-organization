# Crypto-organization
# Django + Celery + Redis Setup Guide

Ensure you have the following installed:
- Python (>=3.8)
- Django
- Redis
- Celery

## Installation Steps

### 1. Install Required Packages

```sh
pip install django celery redis django-celery-beat
```
or 

use requierment.txt to install requierd packages

### 2. Run Django

```sh
py manage.py runserver
```

### 3. Start Redis Server

Ensure Redis is running:

```sh
redis-server
```

### 4. Run Celery Worker

Execute the following command:

```sh
celery -A crypto_project worker --loglevel=info
```

### 5. Running Celery Beat (Optional, for periodic tasks)

```sh
celery -A crypto_project beat --loglevel=info
```


