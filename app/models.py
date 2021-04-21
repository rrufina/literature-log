from django.db import models

# Create your models here.

class Poem(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)

    def __str__(self):
        str_format = f'{self.title} ({self.author})'
        return str_format