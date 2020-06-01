from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 60)
    caption = models.CharField(max_length = 100)
    profile = models.ForeignKey()
    likes = models.IntegerField()
    comments = models.ForeignKey()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

        
    


class Profile(models.Model):
    profile_photo = models.ImageField()
    bio = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.

    def save_profile(self):
        self.save

    def delete_image(self):
        self.delete
    
        

class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    image = models.ForeignKey()

    def __str__(self):
        return self.comment
