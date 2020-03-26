from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,ListView
from .models import WriteBlog,SideWidget
from django import forms


class WriteBlog(CreateView):
    model = WriteBlog
    fields = ('title','category','content')
   
    def form_valid(self,form):
        form.instance.author = self.request.user
        form.save()
        return redirect('/')


class WrInSiWid(CreateView):
    model = SideWidget
    fields = ('content',)

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/')

