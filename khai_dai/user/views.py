from django.shortcuts import render,redirect
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.views.generic import ListView
from order.models import Order,CartItem
from django.views.generic.edit import DeleteView
from django.http import HttpResponseNotFound
# from books.models import Purcehase_history

def sing_up(request):
    if request.method == 'POST':
        sing_up_form = forms.RegistrationForm(request.POST)
        if sing_up_form.is_valid():
            user = sing_up_form.save()
            user.is_active = False
            user.save()

            # Send email verification
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('user/veryfication_mail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, 'Account Created Successfully. Please check your email to activate your account.')
            return redirect('login')

    else:
        sing_up_form = forms.RegistrationForm()
    return render(request, 'user/register.html', {'form': sing_up_form, 'type': 'Register'})

class EmailVerificationView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Email verification successful. You can now log in.')
        else:
            messages.error(request, 'Email verification failed.')
        return HttpResponse("Email verification completed. You can close this tab.")

# This Class based user Login  

class UserLoginViewClass(LoginView):
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'You are successfully logged in')
        # form
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Your provided information is incorrect')
        # form
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

# This Class based user Logout
# @method_decorator(login_required, name= 'dispatch')
def user_logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect(reverse_lazy('homepage'))
    


class OrderListView(ListView):
    model = Order
    template_name = 'all_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()

class OrderItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'order_item_confirm_delete.html'
    success_url = reverse_lazy('all_orders')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Order.DoesNotExist:
            return HttpResponseNotFound("Order not found")