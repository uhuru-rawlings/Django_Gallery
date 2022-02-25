from django.shortcuts import render,redirect
from .models import Location, Category, Images

# Create your views here.
def images_view(request):
    categs = Category.objects.all()
    locat = Location.objects.all()
    if request.method == "POST":
        location = request.POST['location_take']
        images = request.FILES['image_file']
        category = request.POST['categories']
        description = request.POST['image_description']
        new_locs = Location.objects.get(locations = location)
        new_cate = Category.objects.get(categories = category)
        new_post = Images(image_name = images,
                          image_description = description,
                           image_category = categories,
                           location_take = locations
                           )
        new_post.save()
    contex = {
        "title":"Gallery Page | Uploads",
        "categs" : categs,
        "locat":locat
    }
    return render(request, "gallery.html", contex)

def location_view(request):
    if request.method == "POST":
        locate = request.POST['image_locations']
        check_loc = Location.objects.filter(locations = locate).exists()
        if not check_loc:
            new_loc = Location(locations = locate)
            new_loc.save()
        else:
            return redirect('/location/')
    get_loc = Location.objects.all()
    contex = {
        "title": "Gallery-App | Add Location",
        "get_loc": get_loc
    }
    return render(request, "locations.html", contex)

def addcategory_view(request):
    if request.method == 'POST':
        categ = request.POST['image_category']
        get_cat = Category.objects.filter(categories = categ).exists()
        if not get_cat:
            new_category = Category(categories = categ)
            new_category.save()
        else:
            return redirect('/addcategory/')

    all_cats = Category.objects.all()
    contex = {
        "title":"Gallery-App | Add_Category",
        "all_cats": all_cats
    }
    return render(request, "add_category.html", contex)

def delete_category(request, categ_id):
    if request.method == "POST":
        get_det = Category.objects.get(id = categ_id)
        get_det.delete()

        return redirect('/addcategory/')

def delete_location(request, loca_id):
    if request.method == "POST":
        get_locs = Location.objects.get(id = loca_id)
        get_locs.delete()

        return redirect('/location/')