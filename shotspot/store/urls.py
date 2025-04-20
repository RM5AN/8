from django.urls import path
from . import views

urlpatterns = [
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
    path('api/wishlist/toggle/', views.toggle_wishlist, name='toggle_wishlist'),
    path('api/products/search/', views.search_products, name='search_products'),
    path('search/', views.search_view, name='search'),  # صفحة نتائج البحث
]

