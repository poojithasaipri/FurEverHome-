from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('pets/', views.pet_list, name='pet_list'),
    path('logout/', views.logout_view, name='logout'),
    path('add-pet/', views.add_pet, name='add_pet'),
]




