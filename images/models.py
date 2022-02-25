from django.db import models

# Create your models here.
class Location(models.Model):
    locations = models.CharField(max_length=100)
    date_added = models.DateField(auto_now= True)

    class Meta:
        db_table = 'Location' 

    def __str__(self):
        return self.locations

    def save_editor(self):
        self.save()

class Category(models.Model):
    categories = models.CharField(max_length=100)
    date_added = models.DateField(auto_now= True)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.categories
    
    def save_editor(self):
        self.save()

class Images(models.Model):
    images = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=200)
    image_description = models.CharField(max_length=3000)
    location_take = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now= True)

    class Meta:
        db_table = 'Images'


    def save_editor(self):
        self.save()