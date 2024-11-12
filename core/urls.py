from django.urls import path
from .views import Signup, Login, abc, login_view, logout_view, index_view, Adminlogin,index_two, logout_admin
from core import views

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('abc/', views.abc, name='abc'),
    path('Adminlogin/', Adminlogin, name='Adminlogin'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', logout_view, name='logout_view'),
    path('index/', index_view, name='index'),
    path('index_two/',index_two, name='index_two'),
    path('logout_admin/',logout_admin, name='logout_admin'),
]