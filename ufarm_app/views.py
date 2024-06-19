from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.



# Main Views
def agricofficer_home(request):
    return render(request, 'homepages/agricofficer_home.html')

def farmerone_home(request):
    return render(request, 'homepages/farmerone_home.html')

def urbanfarmer_home(request):
    return render(request, 'homepages/urbanfarmer_home.html')


# Login Views
def urbanfarmer_login(request):
    return render(request, 'authentication/urbanfarmer_login.html')

def agricofficer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('agricofficer_home')
        else:
            messages.success(request, "Wrong Credentials")
            return redirect('agricofficer_login')
    return render(request, 'authentication/agricofficer_login.html')

def farmerone_login(request):
    return render(request, 'authentication/farmerone_login.html')





def products(request):
    return render(request, 'products.html')

def home(request):
    return render(request, 'index.html')

