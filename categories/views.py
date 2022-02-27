from django.shortcuts import render,redirect
from django.http import HttpRequest
from images.models import Images,Location,Category
import pyperclip

# Create your views here.
def categories_view(request):
    files = Images.objects.all()
    contex = {
        "title":"Category Page | Gallery",
        "files":files
    }
    return render(request, "category.html", contex)


def get_search(request):
    if request.method == 'POST':
        searchItems = request.POST['searchItems']
        categ_id = Category.objects.filter(categories = searchItems)
        locat_id = Location.objects.filter(locations = searchItems)
        if categ_id.exists():
             categ_id = Category.objects.get(categories = searchItems)
             single_img = Images.objects.filter(image_category_id = categ_id.id)
        elif locat_id.exists():
            categ_id = Location.objects.get(locations = searchItems)
            single_img = Images.objects.filter(location_take_id = categ_id.id)
        else:
            message_error = "Sorry this category do not exist"
            return redirect("/category/")
        
    contex = {
        # "search": single_img,
        "single_img":single_img
    }


    return render(request, "search.html", contex)

def copy_data(request,image_id):
    copied = ""
    single_img = Images.objects.get(id = image_id)
    copied = str(single_img.images)
    pyperclip.copy(copied)
    return redirect("/category/")