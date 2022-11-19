from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User

#         fields = ["email", "username", "first_name", "last_name"]
#         error_class = "error"
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter email...'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password...'})

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','username', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter email...'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        



