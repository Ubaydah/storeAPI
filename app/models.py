from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Wallet(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

class BankAccount(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100, default=True)
    bank_code = models.IntegerField()
    bank_name = models.CharField(max_length=250, default=True)
    created_at = models.DateTimeField(default=timezone.now)