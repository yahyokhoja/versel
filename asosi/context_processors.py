from .models import Category

def menu_categories(request):
    categories = Category.objects.prefetch_related('subcategories')
    return {'menu_categories': categories}
