from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    context = {
        "current_year": datetime.date.today().year,
    }
      
    return render(request, 'index.html', context)

def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        valid = form.is_valid()

        if valid:
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            return redirect('login')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'register.html', {'form': form})

def user_login(request):
    form = UserLoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password.")

    return render(request, "login.html", {"form": form})
