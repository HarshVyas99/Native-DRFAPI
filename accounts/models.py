from django.db import models

# Create your models here.

from authemail.models import EmailUserManager,EmailAbstractUser

class MyUser(EmailAbstractUser):
    first_name = models.CharField(('first name'), max_length=30, blank=True,null=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True,null=True)
    full_name = models.CharField(('full name'), max_length=30, blank=True)
    REQUIRED_FIELDS = []
    objects = EmailUserManager()
