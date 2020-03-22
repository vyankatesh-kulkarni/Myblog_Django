from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup',views.Signup),
    path('login',LoginView.as_view(template_name='blog/login.html')),
    path('logout',LogoutView.as_view())
   # path('login',LoginView.as_view(template_name = 'login.html') , name='login')
]
