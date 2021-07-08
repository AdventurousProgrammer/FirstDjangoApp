from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(response, id):
    t = ToDoList.objects.get(id=id)
    item = t.item_set.get(id=1)
    return HttpResponse(f"<h1>tech with tim! Looking at list: {t.name} it has {item.text}</h1>")

def v1(response):
    return HttpResponse("<h1>View 1!</h1>")