# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from menu.models import FoodItems
from . import models
from . import forms

def place_order(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        total_cost = cart.get_total_price()

        # Subtract discount if available
        discount = 0
        for cart_item in cart.items.all():
            if cart_item.food_item.discounted_price:
                discount += cart_item.food_item.price - cart_item.food_item.discounted_price

        # Calculate the final total cost after applying discounts
        total_cost -= discount

        # Create an order instance
        order = models.Order.objects.create(
            user=request.user,
            total_cost=total_cost
        )

        # Transfer cart items to the order
        for cart_item in cart.items.all():
            order.items.add(cart_item)

        # Clear the user's cart
        cart.items.clear()

        return render(request, 'order_confirmation.html', {'order': order, 'discount': discount, 'total_cost':total_cost})
    else:
        return redirect('login')

def order_history(request):
    if request.user.is_authenticated:
        orders = models.Order.objects.filter(user=request.user)
        return render(request, 'order_history.html', {'orders': orders})
    else:
        return redirect('login')




def submit_review(request, food_item_id):
    if request.user.is_authenticated:
        food_item = FoodItems.objects.get(id=food_item_id)

        if request.method == 'POST':
            form = forms.ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.food_item = food_item
                review.save()
                return redirect('menu_detail', food_item_id=food_item_id)
        else:
            form = forms.ReviewForm()

        return render(request, 'submit_review.html', {'form': form, 'food_item': food_item})
    else:
        return redirect('login')







def add_to_cart(request, food_item_id):
    food_item = FoodItems.objects.get(id=food_item_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, food_item=food_item)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    # Manually add the CartItem to the Cart items set and save the Cart
    cart.items.add(cart_item)
    cart.save()

    return redirect('view_cart')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

def view_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()

        print(f"Cart: {cart}, Created: {created}, Cart Items: {cart_items}")
        return render(request, 'view_cart.html', {'cart': cart, 'cart_items': cart_items})
    else:
        return render(request, 'view_cart.html', {'cart': None})