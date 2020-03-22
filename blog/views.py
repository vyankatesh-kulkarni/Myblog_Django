from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

 
# Create your views here.
def home(request):
    return render(request,'index.html')

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request,'blog/signup.html',{'form':form})


