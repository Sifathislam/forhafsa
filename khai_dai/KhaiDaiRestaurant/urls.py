"""
URL configuration for KhaiDaiRestaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='homepage'),
    path('aboutUs/',views.AboutViewSet.as_view(), name='about_us'),
    path('service/',views.ServiceViewSet.as_view(), name='service'),
    path('booking/',views.BookingViewSet.as_view(), name='booking'),
    path('team/',views.TeamViewSet.as_view(), name='team'),
    path('menu/',views.MenuViewSet, name='menu'),
    path('mainmenu/<slug:brand_slug>/', views.MenuViewSet, name='main_brand_wise'),
    path('testomonail/',views.TestimonialViewSet.as_view(), name='testomonial'),
    path('contact/',views.ContactViewSet.as_view(), name='contact'),
    path('menu/<slug:brand_slug>/', views.home, name='brand_wise'),
    path('User/', include('user.urls')),
    path('Menu/', include('menu.urls')),
    path('Menu/', include('order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)