from django.db import models
from django.utils.timezone import now

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True, blank=True)
    joined_date = models.DateField(default=now)
    
