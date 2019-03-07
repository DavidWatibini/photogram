from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class photogram_TestCases(TestCase):
    def setUp(self):
        self.new_location = Location(location_det = 'London')
        self.new_location.save_location()
        self.new_category = Category(category_det = 'Tech')
        self.new_category.save_category()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_location,Location))
        self.assertTrue(isinstance(self.new_category,Category))

    def test_search_by_category(self):
        self.new_image.save_image()
        instance = Category.objects.get(category_det='Tech')
        self.assertTrue(instance.category_det_name=='Tech')
