from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

    # Можно добавить кастомную валидацию или обработку данных здесь
