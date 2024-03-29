from django.conf import settings
from django.core.cache import cache
from main.models import Category


def get_categories():
    categories = None
    if settings.CACHE_ENABLED:
        key = f'categories'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
    else:
        categories = Category.objects.all()
    return categories
