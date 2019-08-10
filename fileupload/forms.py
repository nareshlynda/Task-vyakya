from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
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


class UserLoginForm(forms.Form):
    username = forms.CharField(label="",
                                widget = forms.TextInput(attrs={'class': 'form-username form-control', 'placeholder': 'Username'}),
                               )
    password = forms.CharField(label="",
                                widget = forms.PasswordInput(attrs={'class': 'form-password form-control', 'placeholder': 'Password'}),
                               )
    def clean(self, *args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username is not None and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("Incorrect Username or Password")
            else:
                if not user.check_password(password):
                    raise forms.ValidationError("Incorrect password")
                if not user.is_active:
                    raise forms.ValidationError("This user no longer active.")
            return super(UserLoginForm,self).clean(*args,**kwargs)