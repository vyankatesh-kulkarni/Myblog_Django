from django.contrib import admin
from django.urls import path
from . import views
from blog.blogviews import *
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Homeview.as_view()),
    path('',views.Homeview.as_view()),
    path('signup',views.Signup),
    path('login',LoginView.as_view(template_name='blog/login.html')),
    path('logout',LogoutView.as_view()),
   # path('login',LoginView.as_view(template_name = 'login.html') , name='login')

    path('writeblog',WriteBlog.as_view()),
    path('sidewidget',WrInSiWid.as_view()),

    path('addCategory',views.AddCategory.as_view()),
]
