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
    image = models.ImageField()
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

    # def all_like(self):
    #     return self.likes

    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(id = id)
        return image 

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(name_contain = search_term)


class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.comment
