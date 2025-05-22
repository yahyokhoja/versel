from django import forms
from store.models import Store

class StoreCreateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'logo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
