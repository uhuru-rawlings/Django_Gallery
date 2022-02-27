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


    def save_image(self):
        self.save()
    def delete_image(self, id):
        self.objects.delete(id = id)

    def update_image(self, id):
        updates = "news_image"
        self.objects.filter(id = id).update(image = updates)

    def get_image_by_id(self, ids):
        self.objects.filter(id = ids)

    def search_image(self, category):
        self.objects.filter(categories = category)

    def filter_by_location(self, location):
        self.objects.filter(locations = location)



# save_image() - Save an image to the database.
# delete_image() - Delete image from the database.
# update_image() - Update image in the database.
# get_image_by_id(id) - Allows us to get an image using its ID.
# search_image(category) - Allows us to search for an image using its category.
# filter_by_location(location) - Allows us to filter images by the location.