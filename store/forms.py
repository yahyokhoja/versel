from django import forms
from .models import Store  # или 'from store.models import Store'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'logo']
