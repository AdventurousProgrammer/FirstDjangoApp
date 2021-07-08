from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(response, id):
    t = ToDoList.objects.get(id=id)
    #item = t.item_set.get(id=1)
    return render(response, "main/base.html", {}) # assuming already in templates folder?

def home(response):
    return render(response, "main/home.html", {})