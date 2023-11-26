from django.contrib import admin
#from myapp.models import employee
#from myapp.models import product
from myapp.models import Products
from myapp.models import Member, ImageModel


# Register your models here.
#admin.site.register(employee)
#admin.site.register(product)
admin.site.register(Member)
admin.site.register(Products)
admin.site.register(ImageModel)
