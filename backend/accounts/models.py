# accounts/models.py
from django.db import models

class Product(models.Model):
    slug = models.SlugField(unique=True, max_length=100)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Django 3.1+ incluye JSONField para SQLite también
    images = models.JSONField(default=list, blank=True)
    features = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    slug = models.SlugField(unique=True, max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    images = models.JSONField(default=list, blank=True)
    features = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title