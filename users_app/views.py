from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm

def register(request):
    if request.method == "POST":
        register_form =CustomRegisterForm(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("your details is saved"))
            return redirect('register')
    else:
        register_form=CustomRegisterForm()
    return render(request,'register.html',{'register_form': register_form})
