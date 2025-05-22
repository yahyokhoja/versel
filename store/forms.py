from django import forms
from .models import Store ,Product # или 'from store.models import Store'



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'subcategory']  # Добавь все необходимые поля модели


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'logo']
