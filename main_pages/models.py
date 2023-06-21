from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='main_pages/images')

    def __str__(self):
        return self.name
