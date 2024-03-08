from django.shortcuts import render
from django.views.generic import FormView
from . import forms
from django.urls import reverse_lazy
from . import models
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
# Create your views here.

class AddFoodItem(FormView):
    template_name = 'Addform.html'
    form_class = forms.FoodItemsForm
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
            form.save()
            return super().form_valid(form)
    



class FoodModelUpdateView(UpdateView):
    model = models.FoodItems
    form_class = forms.FoodItemsForm
    template_name = "Addform.html"
    success_url = reverse_lazy('homepage')



class FoodModelDeleteView(DeleteView):
    model = models.FoodItems
    template_name = "delete.html"
    success_url = reverse_lazy('homepage')
    context_object_name = 'form'

class MenuDetailView(DetailView):
    model = models.FoodItems
    template_name = 'menu_detail.html'
    context_object_name = 'food_item'
    pk_url_kwarg = 'food_item_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.review_set.all()
        return context