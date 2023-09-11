from django.shortcuts import render, redirect
from .forms import UserAuthenticationForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Contact

def index(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        d=Contact(name=name, email=email, message=message)
        d.save()
        return HttpResponse("Message sent successfully")
        
    return render(request, 'index.html', context)


def login_view(request):
    context = {}
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
    return render(request, 'registrations/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            print(email)
            password = form.cleaned_data.get('password1')
            print(password)
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
            # account = authenticate(email=email, password=raw_password)
            # login(request, account)
            # destination = kwargs.get("next")
            # if destination:
            #     return redirect(destination)
            # return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registrations/register.html', context)