from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/confirm_login/', views.confirm_login, name='confirm_login'),
    path('logout/', views.logout, name='logout'),
    path('template1/', views.test_1, name='template1'),
    path('template2/', views.test_2, name='template2'),
]
