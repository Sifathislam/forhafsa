# urls.py
from django.urls import path
from .views import add_to_cart, view_cart,remove_from_cart,place_order,order_history,submit_review

urlpatterns = [
    path('add_to_cart/<int:food_item_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
     path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('place_order/', place_order, name='place_order'),
    path('order_history/', order_history, name='order_history'),
    path('submit_review/<int:food_item_id>/', submit_review, name='submit_review'),
]
