from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/images')

    def __str__(self):
        return self.name
