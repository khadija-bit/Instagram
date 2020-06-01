from django.test import TestCase
from .models import Image,Profile,Comment


# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.khadija = Image(image='khadija')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.khadija,Image))    


class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.khadija = Profile(profile_photo = 'khadija')
    
    # Testing instance
    def test_instance(self):    
        self.assertTrue(isinstance(self.khadija,Profile))