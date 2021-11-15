from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    # email = models.EmailField(_('email address'))
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    document = models.FileField(upload_to="documents/%Y/%m/%d")
    location = models.CharField(max_length=1000, blank=True)
    phone_number = models.CharField(max_length=11)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.username + " / " + self.password