from django.shortcuts import render, redirect
from .models import Note
from .formss import *

def home(request):
    return render(request, 'index.html', {
        'notes': Note.objects.all()
    })


def create_note(request):
    note = NoteForm
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    context = {
        'form': note,
    }
    return render(request, 'maps.html', context)