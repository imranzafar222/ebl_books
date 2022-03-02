import email
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=20, default='fsomeone')
    lname = models.CharField(max_length=20, default='lsomeone')
    email = models.CharField(max_length=40)
    textarea = models.CharField(max_length=200, default='msg')
    date = models.DateTimeField()

    def __str__(self):
        return self.email
