from django.shortcuts import render

# Create your views here.
def home_view(request):
    contex = {
        "title":"Home Page | Gallery"
    }
    return render(request, "index.html", contex)