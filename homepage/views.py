from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from homepage.forms import LoginForm, AddUserForm
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from homepage.models import MyUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logoutview(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            # user.author.name = form.cleaned_data.get('name')
            # user.author.bio = form.cleaned_data.get('bio')
            # user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = AddUserForm()
    return render(request, 'adduser.html', {'form': form})