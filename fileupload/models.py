from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL

class Upload(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name




                 