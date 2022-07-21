from django.urls import path
from todo import views

urlpatterns = [
    path("",views.base,name="base"),
    path("login/",views.login_view,name="login_view"),
    path('signup/',views.signup_view,name="signup_view"),
    path('signup/register_user/',views.register_user,name="register_user"),
    path('login/login_user/',views.login_user,name="login_user"),    
    path("login/logout/", views.logout_view,name="logout_view"),
    path("index/",views.index,name="index"),
    path("index/add_work/",views.add_work,name="add_work"),
    path('index/<int:id>', views.delete, name='delete'),

]