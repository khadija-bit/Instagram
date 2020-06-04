from django import forms
from .models import Profile
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.Form):

    class Meta:
        model = Profile
        fields = ('profile_photo','bio')