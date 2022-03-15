from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    schedule = models.DateTimeField()
