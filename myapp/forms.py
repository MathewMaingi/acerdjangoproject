from django import forms
from myapp.models import employee
from myapp.models import Products, ImageModel


class employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['firstname', 'lastname', 'email', 'password', 'age']
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'origin', 'color']

class ImageUploadForm(forms.ModelForm):
     class Meta:
           model = ImageModel
           fields = ['image', 'title', 'price']