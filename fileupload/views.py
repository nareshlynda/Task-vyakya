from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UploadForm, UserLoginForm
from .models import Upload
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def upload(request):
        form = UploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/prevupload/')
       
     
        return render(request, 'fileupload/upload.html', {'form' : form})

def prevupload(request):
    files = Upload.objects.all()
    context = {
        'files' : files
    }
    return render(request, 'fileupload/prevupload.html', context)    



def download(request):
    files = Upload.objects.all()
    context = {
        'files' : files
    }
    return render(request, 'fileupload/download.html', context)    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'fileupload/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(request.user)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    if request.user.is_superuser:
                        return redirect('/upload/')
                    else:
                        return redirect('/download/')
        else:
            print("invalid")  
            print(request.POST)              
    else:
        form = UserLoginForm()
    return render(request,'fileupload/login.html', {'form':form})    

