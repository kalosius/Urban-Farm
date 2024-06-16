from django.shortcuts import render

# Create your views here.



# Login Views
def urbanfarmer_login(request):
    return render(request, 'authentication/urbanfarmer_login.html')

def agricofficer_login(request):
    return render(request, 'authentication/agricofficer_login.html')

def farmerone_login(request):
    return render(request, 'authentication/farmerone_login.html')





def products(request):
    return render(request, 'products.html')

def home(request):
    return render(request, 'index.html')

