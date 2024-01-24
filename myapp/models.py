from django.db import models

# Create your models here.

class Email(models.Model):
    Subject = models.CharField(max_length=500)
    From = models.CharField(max_length=500)
    To = models.TextField()
    Cc = models.TextField( default='')
    Bcc = models.TextField( default='')
    Content = models.TextField()
