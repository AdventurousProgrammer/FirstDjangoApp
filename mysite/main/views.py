from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.
def index(response, id):
    t = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":t}) # assuming already in templates folder?

def home(response):
    return render(response, "main/home.html", {"name":"test"})

def create(response):
    form = CreateNewList()
    return render(response, "main/create.html", {"form":form})
