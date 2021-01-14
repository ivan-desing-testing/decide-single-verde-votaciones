from django.db import models

# Create your models here.
class Suggestion(models.Model):
    suggestion = models.TextField()

def __str__(self):
        return self.suggestion
