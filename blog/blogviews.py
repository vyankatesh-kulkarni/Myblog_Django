from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,ListView,DeleteView,UpdateView,DetailView
from blog.models import WriteBlog,SideWidget
from django import forms
from . forms import WriteBlogForm


class Writeblog(CreateView):
    model = WriteBlog
    #fields = ('title','category','content')
    form_class = WriteBlogForm
   
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


class ReadBlog(DetailView):
    #pid = request.GET.get('id')
    #print('id =>',pid)
    #post  = WriteBlog.objects.get(id = pid)
    #return render(request,'readblog.html',{'post':post})
    model = WriteBlog
    template_name = 'blog/blog_detail.html'
    
  
