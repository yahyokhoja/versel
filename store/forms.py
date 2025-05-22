from django import forms
from .models import Store ,Product # или 'from store.models import Store'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'subcategory']  # ✅ верные поля





class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'logo']
