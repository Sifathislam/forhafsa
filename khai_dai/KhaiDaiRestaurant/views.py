from django.shortcuts import render
from menu.models import FoodItems
from category.models import Category
from django.views.generic import TemplateView

def home(request, brand_slug=None):
    data = FoodItems.objects.all()
    specials = FoodItems.objects.filter(discounted_price__isnull=False)  # Add this line for specials
    if brand_slug is not None:
        brand_name = Category.objects.get(slug=brand_slug)
        data = FoodItems.objects.filter(category=brand_name)

    brands = Category.objects.all()

    return render(request, 'home.html', {'data': data, 'brands': brands, 'specials': specials})




class AboutViewSet(TemplateView):
    template_name = "about.html"

class ServiceViewSet(TemplateView):
    template_name = "service.html"
    
class TeamViewSet(TemplateView):
    template_name = "team.html"

class TestimonialViewSet(TemplateView):
    template_name = "testimonial.html"
    
class ContactViewSet(TemplateView):
    template_name = "contact.html"

def MenuViewSet(request, brand_slug=None):
    data = FoodItems.objects.all()
    specials = FoodItems.objects.filter(discounted_price__isnull=False)  # Add this line for specials
    if brand_slug is not None:
        brand_name = Category.objects.get(slug=brand_slug)
        data = FoodItems.objects.filter(category=brand_name)

    brands = Category.objects.all()

    return render(request, 'menu.html', {'data': data, 'brands': brands, 'specials': specials})

class BookingViewSet(TemplateView):
    template_name = "booking.html"