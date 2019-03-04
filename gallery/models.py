from django.db import models


# Create your models here.

#for category_det

class Category(models.Model):
    category_det = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.category_det

#for location_det

class Location(models.Model):
    location_det = models.CharField(max_length=50)

    def __str__(self):
        return self.location_det

class Image(models.Model):
    image_name = models.CharField(max_length =50)
    image_description = models.TextField()
    image_location = models.ImageField(upload_to = 'images/')
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
