from django.db import models
from django.contrib.auth.models import User
from category.models import Category
# Create your models here.
class FoodItems(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, null = True , blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='menu/uploads', height_field=None, width_field=None, max_length=None,default='')
        
    def __str__(self):
            return self.name

class review(models.Model):
    post = models.ForeignKey(FoodItems, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"reviwe by {self.name}"

class Order_history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    FoodItems = models.ForeignKey(FoodItems,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} borrowed this book name: {self.Book.title}"