from django import forms

class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='Email')

class UserUpdateForm(forms.Form):
    email = forms.EmailField(label='Email')