from django.urls import path
from homepage import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('adduser.html', views.add_user, name='adduser'),
    path('homepage.html', views.homepage, name='homepage')
]