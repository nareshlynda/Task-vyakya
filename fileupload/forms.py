from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Upload
#from django.forms import ModelForm

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['name','description','upload'] 






class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


     
       