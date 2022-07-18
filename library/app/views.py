from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import User
from .forms import MyUserCreationForm,MyUserChangeForm



def signup(request):
   form = MyUserCreationForm()
   
   if request.method == 'POST':
       form = MyUserCreationForm(request.POST)
       if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                    password=request.POST['password1'])
            login(request, user)
            return redirect('home')

   return render(request, 'registration/signup.html', { 'form':  form})


def profile(request):
    if request.method =='POST':
        form = MyUserChangeForm(request.POST,instance= request.user)
        if form.is_valid():
            form.save()
    form = MyUserChangeForm(instance= request.user)
    return render(request, 'registration/profile.html',{'form':form})