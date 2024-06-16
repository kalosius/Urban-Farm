from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),


    # Authentication urls
    # Login Urls
    path('urbanfarmer_login/', views.urbanfarmer_login, name="urbanfarmer_login"),
    path('agricofficer_login/', views.agricofficer_login, name="agricofficer_login"),
    path('farmerone_login/', views.farmerone_login, name="farmerone_login")

]