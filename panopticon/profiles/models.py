from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    email = models.EmailField(max_length=100)
    display_name = models.CharField(max_length=50, unique=True,
        validators=[
            RegexValidator(regex=r'("")|(^[a-z0-9_]+$)',
                           message='Please only a-z characters, numbers and '
                                   'underscores.')])
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=True)
    member = models.BooleanField(default=False)
    phone = models.CharField(max_length=14, blank=True)
    fullsub = models.BooleanField(default=True)
    subtill = models.DateField(auto_now_add=True)
    accountant = models.BooleanField(default=False)
