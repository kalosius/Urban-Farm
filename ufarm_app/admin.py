from django.contrib import admin
from . models import UrbanWard, FarmerOne, UrbanFarmer, Product

# Register your models here.
admin.site.register(UrbanWard)
admin.site.register(FarmerOne)
admin.site.register(UrbanFarmer)
admin.site.register(Product)