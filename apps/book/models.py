from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    nationality = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(('Created date'), auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    publish_date = models.DateField('Publication date', blank=False, null=False)
    author_id = models.ManyToManyField(Author)
    created_date = models.DateField(('Created date'), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
