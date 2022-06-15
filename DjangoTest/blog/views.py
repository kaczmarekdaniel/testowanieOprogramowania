from django.shortcuts import render
from blog.models import Item

def home_page(request):
    if request.POST:
        item = Item()
        item.text = request.POST['id_new_item']
        item.save()

    return render(request, "home.html", {"items": Item.objects.all()})