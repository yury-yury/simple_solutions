from django.shortcuts import render

from .models import Item


def view_item(request, id: int):
    item = Item.objects.get(pk=id)
    return render(request, 'main/base.html', {'item': item})