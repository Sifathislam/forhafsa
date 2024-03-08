from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.FoodItems)
admin.site.register(models.Order_history)
admin.site.register(models.review)