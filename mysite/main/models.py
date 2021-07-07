from django.db import models

class ToDoList(models.Model): # database object, entry attribute
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    # remove todolist when ToDoLIst table is deleted, models.CASCADE special way of removing
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # automatically creates a set of items called item_set under todolist instance                    # related to ToDoList, one to do list many items
    # this relation allows ToDoList instance to access item in the following way: t.item_set.all()
    # t.item_set.get(query) to get an item instance
    # READ DOCUMENTATION
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __repr__(self):
        return self.text
# Create your models here.
