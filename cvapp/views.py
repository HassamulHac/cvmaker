from django.shortcuts import render, get_object_or_404, redirect
from .models import CV
from .forms import CVForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

def cv_list(request):
    cvs = CV.objects.all()
    return render(request, 'cvapp/cv_list.html', {'cvs': cvs})

def cv_detail(request, cv_id):
    cv = get_object_or_404(CV, pk=cv_id)
    return render(request, 'cvapp/cv_detail.html', {'cv': cv})

def delete_cv(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    cv.delete()
    return redirect('cv_list')
    
def welcome_view(request):
    return render(request, 'cvapp/welcome.html')  # Create a welcome.html template

from django.shortcuts import render, redirect
from .forms import  CVForm

def create_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cv_list')  # You can define a success URL in your urls.py
    else:
        form = CVForm()

    return render(request, 'cvapp/create_cv.html', {'form': form})

'''
def signup_or_login(request):
    signup_form = SignUpForm()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                messages.success(request, 'Account created successfully. You are now logged in.')
                return redirect('welcome')  # Redirect to welcome.html after signup
        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('welcome')  # Redirect to welcome.html after login
                else:
                    messages.error(request, 'Invalid login credentials.')

    return render(request, 'cvapp/signup_or_login.html', {'signup_form': signup_form, 'login_form': login_form})
    '''
