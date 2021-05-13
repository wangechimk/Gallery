from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

    def save_category(self):
        self.save()
    

class Images(models.Model):
    image_link = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)

# add image categories model
    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    

class Locations(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    def save_location(self):
        self.save()    