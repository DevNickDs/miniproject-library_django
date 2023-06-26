from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    nationality = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    