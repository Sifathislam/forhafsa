from django import forms
from . import models

class FoodItemsForm(forms.ModelForm):
    class Meta:
        model = models.FoodItems
        fields = '__all__'
        
class reviewForm(forms.ModelForm):
    class Meta: 
        model = models.review
        fields = ['name', 'body']