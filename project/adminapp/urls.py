from django.urls import path
from adminapp import views
urlpatterns = [
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
] 
