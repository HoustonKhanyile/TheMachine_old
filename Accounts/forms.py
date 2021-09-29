from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth


class CreateUserForm(UserCreationForm):

    Birth_Date = forms.DateField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'Birth_Date', 'email', 'password1', 'password2',]
        
        def clean_username(self):
            username = self.cleaned_data.get("username")
            if User.objects. filter(username=username).exists():
                raise forms.ValidationError("Username is not unique")
            return username

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects. filter(email=email).exists():
                raise forms.ValidationError("Email is not unique")
            return email