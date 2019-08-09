from django.db import models

class Upload(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

                 