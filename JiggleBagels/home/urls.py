from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'home'

urlpatterns = [
    # path('signout/', views.signout, name="signout"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home/index.html'), name='logout'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html', authentication_form=LoginForm), name='login'),
]
