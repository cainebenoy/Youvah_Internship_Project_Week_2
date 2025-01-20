from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required  # Ensures only logged-in users can access this page
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            messages.success(request, 'You have signed up successfully.')
            return redirect('index')  # Redirect to the index page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':  # If the form is submitted
        username = request.POST['username']  # Get username from the form
        password = request.POST['password']  # Get password from the form
        user = authenticate(request, username=username, password=password)  # Authenticate user
        if user is not None:  # If authentication is successful
            login(request, user)  # Log the user in
            messages.success(request, 'Login successful!')  # Display success message
            return redirect('index')  # Redirect to the homepage
        else:
            messages.error(request, 'Invalid credentials.')  # Display error message
    return render(request, 'login.html')  # Render login page for GET or failed POST
def logout_user(request):
    logout(request)  # Log the user out
    messages.success(request, 'You have been logged out.')  # Display logout message
    return redirect('login')  # Redirect to the login page
