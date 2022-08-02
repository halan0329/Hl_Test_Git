from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.TextField(primary_key=True)
    pwd = models.TextField()
    phone = models.CharField(max_length=50)
    rdate = models.DateTimeField()
    udate = models.DateTimeField()