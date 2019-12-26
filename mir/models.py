from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Register(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    parentage=models.CharField(max_length=50)
    address=models.CharField(max_length=70)
    email=models.EmailField(max_length=254)
    contact=models.CharField(max_length=50)
    reg_date=models.CharField(max_length=50)

    def publish(self):
        self.reg_date = timezone.now()
        self.save()
    def __str__(self):
        return self.fname

