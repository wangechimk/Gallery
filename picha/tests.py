from django.test import TestCase
from .models import Images, Category, Locations


# Create your tests here.
class ImagesTest(TestCase):
    '''
    '''
    def setUp(self):
        self.new_category = Category(name='testing')
        self.new_category.save()

        self.new_location = Locations(city='Nairobi', country='Kenya')
        self.new_location.save()

        self.new_picture = Images(image_link='images/picture.jpeg', title='Image title', description='sth random', category=self.new_category, location=self.new_location)
        self.new_picture.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_picture,Images))

    def tearDown(self):
        Category.objects.all().delete()
        Locations.objects.all().delete()
        Images.objects.all().delete() 