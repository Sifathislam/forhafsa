from django.urls import path
from .views import AddFoodItem,FoodModelDeleteView,FoodModelUpdateView,MenuDetailView

urlpatterns = [
    path('add_food/', AddFoodItem.as_view(), name='add_food'),
     path('editNote<int:pk>/', FoodModelUpdateView.as_view(), name='EditFood'),
    path('deleteNote<int:pk>/', FoodModelDeleteView.as_view(), name='deleteFood'),
    path('menu_detail/<int:food_item_id>/', MenuDetailView.as_view(), name='menu_detail'),
]
