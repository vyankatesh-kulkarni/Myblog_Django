from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from blog import blogviews
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Homeview.as_view()),
    path('',views.Homeview.as_view()),
    path('signup',views.Signup),
    path('login',LoginView.as_view(template_name='blog/login.html')),
    path('logout',LogoutView.as_view()), 
    #path('sortBlogs',views.sortBlogs),                                  ## To sort blogs on homepage  
    path('sortBlogs/<str:pk>',views.Homeview.as_view()),
 
    # Blog operations
    path('writeblog',blogviews.Writeblog.as_view()),
    path('sidewidget',blogviews.WrInSiWid.as_view()),
    path('editblog',blogviews.bloglist),
    path('deleteblog/<int:pk>',blogviews.DeleteBlog.as_view()),
    path('editblog/<int:pk>',blogviews.EditBlog.as_view()),
    path('readmore/<int:pk>',blogviews.ReadBlog.as_view()),

    # Category
    path('addCategory',views.AddCategory.as_view()),
    path('categorylist',views.CategoryList.as_view()),
    path('deletecat/<str:pk>',views.DeleteCategory.as_view()),
]

