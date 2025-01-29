from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

# 🔹 Function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_staff

# 🔹 Registration View
def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})

# 🔹 Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.', extra_tags='danger')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})

# 🔹 Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# 🔹 Dashboard View (Restricted to Logged-in Users)
@login_required
def dashboard(request):
    return render(request, 'ol_app/dashboard/dashboard.html') 

# 🔹 Map View (Restricted to Admin Users Only)
# @login_required
# def map_view(request):
#     return render(request, 'map/map_only.html')
