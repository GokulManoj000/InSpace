from django.urls import path
from . import views 

urlpatterns=[ 
    path('',views.index,name="index"),
    path('register',views.register, name="register"),
    path('stud_login',views.stud_login,name="stud_login"),
    path('logout',views.user_logout,name='logout'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('submit_homework/', views.submit_homework, name='submit_homework'),
    path('delete_homework/', views.delete_homework, name='delete_homework'),




]