from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.
def index(response, id):
    print(f'Entering Index View')
    t = ToDoList.objects.get(id=id)
    print(type(response))
    print(response == HttpResponse)
    if response.method == 'POST':
        if response.POST.get("save"):
            print(f'response object type: {type(response)}')
            for item in t.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    print(f'Saved Item: {item.id}')
                    item.complete = True
                else:
                    item.complete = False
        elif response.POST.get("newItem"): # custom form so cannot do is valid
            text = response.POST.get("new")
            if len(text) > 2:
                t.item_set.create(text=text, complete=False)
            else:
                print('Invalid Input')
            pass

    return render(response, "main/list.html", {"ls":t}) # assuming already in templates folder?

def home(response):
    return render(response, "main/home.html", {"name":"test"})

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect(f"/{t.id}")
    form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

