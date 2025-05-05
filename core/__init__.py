# -*- encoding: utf-8 -*-


#__CELERY__
from .celery import app as celery_app

__all__ = ('celery_app',)


