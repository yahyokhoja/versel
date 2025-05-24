from django import forms
from .models import Order, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']
        labels = {
            'product': 'Товар',  # Переводим поле product
            'quantity': 'Количество',  # Переводим поле quantity
        }

    def __init__(self, *args, **kwargs):
        store = kwargs.pop('store', None)  # Получаем магазин из аргументов
        super().__init__(*args, **kwargs)
        if store:
            # Фильтруем товары, чтобы отображались только из указанного магазина
            self.fields['product'].queryset = Product.objects.filter(store=store)