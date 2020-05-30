from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 60)
    caption = models.CharField(max_length = 60)
    profile = models.ForeignKey(e)
    likes = models.ForeignKey()
    comments = models.ForeignKey()
    date = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    profile_photo
    bio