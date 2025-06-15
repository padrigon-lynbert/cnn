from django.shortcuts import render
from .forms import PersonForm

def get_name(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            
            return render(request, "thanks.html", {"name": person.name, "age": person.age})
    else:
        form = PersonForm()

    return render(request, "name.html", {"form": form})
