from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

tasks = ["tarea 1", "tarea dos", "tarea 3"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Nueva Tarea con forms.Form")
    #priority = forms.IntegerField(label="Prioridad de Tarea", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request,"tasks/index.html",{
        "tasks" : tasks
    })
    #return HttpResponse("Hello, TASKS")

def add(request):
    if request.method == "POST":
        form= NewTaskForm(request.POST)
        if form.is_valid:
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("index"))
        else:    
            return render(request,"tasks/add.html",{
                "form":form
            })  
    return render(request,"tasks/add.html",{
        "form":NewTaskForm()
    })