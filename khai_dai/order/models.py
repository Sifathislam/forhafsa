# models.py
from django.db import models
from menu.models import FoodItems
from django.contrib.auth.models import User

class CartItem(models.Model):
    Item_cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items' ,null=True, blank =True)  # Specify related_name
    food_item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.food_item.price * self.quantity
    
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank =True,null = True)
    items = models.ManyToManyField(CartItem)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

START_CHOICES = [
    ('★',1),
    ('★★',2),
    ('★★★',3),
    ('★★★★',4),
    ('★★★★★',5),
    ('★★★★★★',6),
    ('★★★★★★★',7),
]
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    rating = models.CharField(choices = START_CHOICES ,max_length=50)
    comment = models.TextField()