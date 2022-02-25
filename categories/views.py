from django.shortcuts import render,redirect
from django.http import HttpRequest
from images.models import Images,Location,Category
import pyperclip

# Create your views here.
def categories_view(request):
    files = Images.objects.all()
    # contex = {
    #     # "title":"Category Page | Gallery",
    #     "files":files
    # }
    return render(request, "category.html", {"files":files})


def get_search(request,image_id):
    single_img = Images.objects.get(id = image_id)
    get_lication = Location.objects.get(id = single_img.id)
    get_category = lication = Category.objects.get(id = single_img.id)
    contex = {
        "search": single_img,
        "get_lication": get_lication,
        "get_category": get_category,
    }


    return render(request, "search.html", contex)

def copy_data(request,image_id):
    copied = ""
    single_img = Images.objects.get(id = image_id)
    copied = str(single_img.images)
    pyperclip.copy(copied)
    return redirect("/category/")