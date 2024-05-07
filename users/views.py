from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, "login.html",{})

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        if password == confirm_password:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('login')
            except:
                error_message = "Error creating account"
                return render(request, 'signup.html', {'error_message': error_message})
        else:        
            return render(request, "signup.html",{"error":"Passwords do not match"})
    return render(request, "signup.html",{})

def logout_view(request):
    logout(request)
    return redirect ('login')

