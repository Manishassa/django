
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Register.html')

        # Check if username already exists
        if Register.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'Register.html')

        # Check if email already used
        if Register.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'Register.html')

        # Create the user in Register model
        user = Register(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'Register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists
        user = Register.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = username
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'Login.html')

    return render(request, 'Login.html')

def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    messages.success(request, "Logged out successfully!")
    return redirect('register')
