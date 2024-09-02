from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='home'),
    path('about/', views.about, name='about'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name ='login')
]

