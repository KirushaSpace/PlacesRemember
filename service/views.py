from django.shortcuts import render, redirect
from .models import Note
from .formss import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def page_not_found_view(request, exception):
    return redirect('login')


@login_required(login_url='/login')
def home(request):
    return render(request, 'index.html', {
        'notes': Note.objects.filter(user=request.user)
    })


@login_required(login_url='/login')
def create_note(request):
    note = NoteForm
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
        return redirect("home")

    context = {
        'form': note,
        'notes': Note.objects.filter(user=request.user)
    }
    return render(request, 'maps.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')


@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect('login')