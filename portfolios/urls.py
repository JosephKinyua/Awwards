from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'welcome'),
    path('account/profile', views.profile, name='profile'),
] 