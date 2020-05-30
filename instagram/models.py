from django.db import models

# Create your models here.
class Image(models.Model):
    Image = models.ImageField()
    name = models.CharField(max_length = 60)
    caption = models.CharField(max_length = 60)
    profile = models.ForeignKey(Profile)
    likes = models.ForeignKey()
    comments = models.ForeignKey()
    date = models.DateTimeField(auto_now_add=True)



