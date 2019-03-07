from django.db import models


# Create your models here.

#for category_det

class Category(models.Model):
    category_det = models.CharField(max_length=50)

    def __str__(self):
        return self.category_det

    def save_category(self):
        self.save()

#for location_det

class Location(models.Model):
    location_det = models.CharField(max_length=50)

    def __str__(self):
        return self.location_det

    def save_category(self):
        self.save()

class Image(models.Model):
    image_name = models.CharField(max_length =30,default='random')
    image_description = models.TextField()
    image_path = models.ImageField(upload_to = 'gallery/')
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):

        search_result = cls.objects.filter(image_category__category_det__icontains=search_term)
        return search_result

    @classmethod
    def update_image(cls,current,new):
        new_instance = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return new_instance

    @classmethod
    def get_image_by_id(cls,new_id):
        image_result = cls.objects.get(id=new_id)
        return image_result

    @classmethod
    def search_by_location(cls,search_term):

        search_result = cls.objects.filter(image_location__location_det__icontains=search_term)
        return search_result
