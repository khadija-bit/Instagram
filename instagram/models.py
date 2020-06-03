from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField()
    bio = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    images = models.ImageField()
    name = models.CharField(max_length = 60)
    caption = models.CharField(max_length = 100)
    likes = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(name__icontains = search_term)
        return images

class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.comment

class NewsLetterEnts(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()