from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def person_list(request):
    persons = Person.objects.all()
    return render(request, "myapp/person_list.html", {"persons": persons})

def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(**form.cleaned_data)
            return redirect("person_list")
    else:
        form = PersonForm()

    return render(request, "myapp/person_create.html", {"form": form})
