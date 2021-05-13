from django.db import models

# Create your models here.
#category model
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, search_term , new_cat):
        try:
            to_update = Category.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Category.DoesNotExist:
            print('Category you specified does not exist')

#image model
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

    @classmethod
    def update_image(cls, search_term , new_link):
        try:
            to_update = Images.objects.get(title = search_term)
            to_update.image_link = new_link
            to_update.save()
            return to_update
        except Images.DoesNotExist:
            print('Image you specified does not exist')    
    

    @classmethod
    def get_image_by_id(cls, id):
        retrieved = Images.objects.get(id = id)
        return retrieved

    @classmethod
    def search_image(cls, category):
        retrieved = Images.objects.get(category=category)
        return retrieved    

#locations model
class Locations(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    def save_location(self):
        self.save()    

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, search_term , new_locale):
        try:
            to_update = Locations.objects.get(country = search_term)
            to_update.city = new_locale
            to_update.save()
            return to_update
        except Locations.DoesNotExist:
            print('Location you specified does not exist') 
    