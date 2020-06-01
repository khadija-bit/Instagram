from django.test import TestCase
from .models import Image,Profile


# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.khadija = Image(image='khadija')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.khadija,Image))    

    # Testing Save Method
    def test_save_method(self):
        self.khadija.save_image()
        pic = Image.objects.all()
        self.assertTrue(len(pic) > 0)    

class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.khadija = Profile(profile_photo = 'khadija')
    
    # Testing instance
    def test_instance(self):    
        self.assertTrue(isinstance(self.khadija,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.khadija.save_profile()
        picture = Profile.objects.all()
        self.assertTrue(len(picture) > 0)     