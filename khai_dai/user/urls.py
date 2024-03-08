from django.urls import path
from . import views
urlpatterns = [
    path('email_verification/<str:uidb64>/<str:token>/', views.EmailVerificationView.as_view(), name='email_verification'),
    path('sing_up/', views.sing_up, name='register'),
    path('login/',views.UserLoginViewClass.as_view(), name = 'login'),
    path('logout/',views.user_logout_view, name = 'logout'),
    path('all_orders/', views.OrderListView.as_view(), name='all_orders'),
    path('order_item/<int:pk>/delete/', views.OrderItemDeleteView.as_view(), name='delete_order_item'),
]
