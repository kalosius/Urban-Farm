from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),


    # Authentication urls
    # Login Urls
    path('urbanfarmer_login/', views.urbanfarmer_login, name="urbanfarmer_login"),
    path('agricofficer_login/', views.agricofficer_login, name="agricofficer_login"),
    path('farmerone_login/', views.farmerone_login, name="farmerone_login"),
    path('farmer_registration/', views.farmerone_registration, name="farmerone_registration"),

    # Registration urls

    # main urls
    path('agricofficer_home/', views.agricofficer_home, name="agricofficer_home"),
    path('farmerone_home/', views.farmerone_home, name="farmerone_home"),
    path('urbanfarmer_home/', views.urbanfarmer_home, name="urbanfarmer_home"),

    

]