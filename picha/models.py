from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

class Images(models.Model):
    image_link = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
# add image categories model
    def __str__(self):
        return self.title
