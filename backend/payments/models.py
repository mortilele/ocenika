from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class CPTransactionManager(models.Manager):
#
#
# class CPTransaction(models.Model):
#     """
#     Cloud Payments transaction model
#     """
#
#     UNKNOWN = 'UNKNOWN'
#     SECURE3D = 'SECURE3D'
#     SUCCESS = 'SUCCESS'
#     FAIL = 'FAIL'
#
#     CP_STATUSES = (
#         (UNKNOWN, UNKNOWN),
#         (SECURE3D, SECURE3D),
#         (SUCCESS, SUCCESS),
#         (FAIL, FAIL),
#     )
#
#     class Meta:
#         verbose_name = 'Платеж (cloud payments)'
#         verbose_name_plural = 'Платежи (cloud payments)'
#
#     order_id = models.CharField(max_length=100, db_index=True)
#     transaction_id = models.CharField(max_length=100, unique=True)
#     account_id = models.CharField(max_length=100)
#     email = models.CharField(max_length=1000)
#     amount = models.FloatField()
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     confirm_date = models.DateTimeField(null=True)
#     status = models.CharField(max_length=20, choices=CP_STATUSES, default=UNKNOWN)
#
#     objects = CPTransactionManager()
#
#     def __str__(self):
#         return

