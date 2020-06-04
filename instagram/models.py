from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField()
    bio = models.CharField(max_length = 60)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def search_profile(cls,search_term):
        user = cls.objects.filter(user__icontains = search_term)
        return user


class Image(models.Model):
    images = models.ImageField()
    name = models.CharField(max_length = 60)
    caption = models.CharField(max_length = 100)
    likes = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def likes_total(self):
        self.likes.count()

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(name__icontains = search_term)
        return images

    @classmethod
    def all_comment(self):
        return self.comment.all() 

class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment(cls):
        comment = cls.objects.all()
        return comment
        

class NewsLetterEnts(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()