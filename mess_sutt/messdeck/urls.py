from django.contrib import admin
from django.urls import path,re_path
from . import views
from .forms import LoginForm

urlpatterns = [
    #path('', views.login, name='messdeck-login'),
    path('', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='messdeck/login.html',authentication_form=LoginForm), name='login'),
    # path('home/logout/', views.logout_view, name='messdeck-logout'),
    # path('home/profile/logout/', views.logout_view, name='messdeck-logout'),
    re_path(r'logout/', views.logout_view, name='messdeck-logout'),
    path('home/', views.home, name='messdeck-home'),
    path('register/', views.RegisterView.as_view(), name='messdeck-register'), 
    path('home/load_data/', views.load_data, name='load_data'),
    path('home/profile/', views.profile, name='messdeck-profile'),
    path('home/menu', views.viewmenu, name='view_menu'),
    path('home/feedback/', views.feedback, name='feedback'),
    # path('feedback_success/', views.feedback_success, name='feedback_success'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),
    path('home/attendance/', views.markattendance, name='attendance'),
]

