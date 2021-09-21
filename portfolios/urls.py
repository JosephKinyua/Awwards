from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'welcome'),
    path('account/profile', views.profile, name='profile'),
    path('account/postproject', views.postpoject, name='postproject'),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),
    path('projectdetails/<int:id>/', views.projectdetails, name='projectdetails'), 
] 