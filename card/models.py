from django.db import models


# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=200, unique=True)
    meaning = models.CharField(max_length=255)
    sentence = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

