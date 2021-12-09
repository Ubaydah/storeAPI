from os import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    firstname = models.CharField(max_length=250, null=True)
    lastname = models.CharField(max_length=250, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Wallet(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

class BankAccount(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100, default=True)
    bank_code = models.IntegerField()
    bank_name = models.CharField(max_length=250, default=True)
    created_at = models.DateTimeField(default=timezone.now)

class Store(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default=True)
    description = models.TextField(max_length=300, default=True)
    currency = models.CharField(max_length=250)
    can_document = models.FileField(upload_to=None, max_length=254)
    owner_id_document = models.FileField(upload_to=None, max_length=254)
    created_at = models.DateTimeField(default=timezone.now, null=True)

class Product(models.Model):
    
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default=True)
    description = models.TextField(max_length=300, default=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)


class Transactions(models.Model):

    TRANSACION_TYPES = (
        ('deposit', 'deposit'),
        ('transfer', 'transfer'),
        ('withdraw', 'withdraw'),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=400, decimal_places=2)
    description = models.TextField(max_length=300)
    timestamp = models.DateTimeField(default=timezone.now)
    transaction_type = models.CharField(max_length=200, null=True, choices=TRANSACION_TYPES)