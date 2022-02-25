from django.contrib import admin
from images.models import Images,Category,Location
# Register your models here.
admin.site.register(Images)
admin.site.register(Category)
admin.site.register(Location)