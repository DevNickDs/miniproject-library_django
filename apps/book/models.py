from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    nationality = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return self.name