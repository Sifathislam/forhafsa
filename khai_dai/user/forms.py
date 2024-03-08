from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount, USER_TYPE

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    User_Type = forms.ChoiceField(choices=USER_TYPE, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'User_Type']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit:
            our_user.save()
            UserAccount.objects.create(user=our_user, User_Type=self.cleaned_data['User_Type'])
        return our_user
