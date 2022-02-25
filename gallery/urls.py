"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home_view
from categories.views import categories_view,get_search,copy_data
from images.views import images_view,location_view,addcategory_view,delete_category,delete_location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = "Home"),
    path('category/', categories_view, name = "category"),
    path('search/<int:image_id>', get_search, name = "search"),
    path('uploaded/', images_view, name = "uploaded"),
    path('addcategory/', addcategory_view, name = "addcategory"),
    path('location/', location_view, name = "locations"),
    path('copy/<str:image_id>/', copy_data, name="copypaste"),
    path('delete_category/<int:categ_id>', delete_category, name="delete_category"),
    path('delete_location/<int:loca_id>', delete_location, name = "delete_location")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)