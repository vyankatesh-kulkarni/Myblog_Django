from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,ListView,DeleteView,UpdateView
from blog.models import WriteBlog,SideWidget
from django import forms


class Writeblog(CreateView):
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

def bloglist(request):
    ls = WriteBlog.objects.all()
    return render(request,'blog/bloglist.html',{'object_list':ls})



class DeleteBlog(DeleteView):
    model = WriteBlog
    success_url = '/'


class EditBlog(UpdateView):
    model = WriteBlog
    fields = ('title','content')
    template_name = 'blog/editblog.html'
    success_url = '/'


def ReadBlog(request):
    pid = request.GET.get('id')
    print('id =>',pid)
    post  = WriteBlog.objects.get(id = pid)
    return render(request,'readblog.html',{'post':post})

