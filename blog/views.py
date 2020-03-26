from django.shortcuts import render,redirect,reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import WriteBlog,Category,SideWidget
from django.views.generic import FormView,DetailView,ListView,CreateView
from django.contrib.auth.forms import UserCreationForm

 
# Create your views here.
class Homeview(ListView):
    model = WriteBlog
    template_name = 'index.html'
    queryset     = WriteBlog.objects.all()

    def get_context_data(self,**kwargs):
        context = super(Homeview,self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sidewidget'] = SideWidget.objects.all()
        return context

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request,'blog/signup.html',{'form':form})


############# category

class AddCategory(CreateView):
    model  = Category
    fields = '__all__'
    template_name = 'blog/addcategory.html'

    def form_valid(self,form):
        form.save()
        return redirect('/')

##### side widget