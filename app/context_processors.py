from .models import Store

def menu_categories(request):
    stores = Store.objects.prefetch_related('categories__subcategories').all()
    return {'menu_categories': stores}
