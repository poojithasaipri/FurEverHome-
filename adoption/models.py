from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, default='Dog')

    age = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
