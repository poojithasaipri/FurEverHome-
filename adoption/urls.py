from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('pets/', views.view_pets, name='view_pets'),
    path('logout/', views.logout_view, name='logout'),
    path('add-pet/', views.add_pet, name='add_pet'),
    path('pets/', views.view_pets, name='view_pets'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('pets/<int:pet_id>/adopt/', views.adopt_pet, name='adopt_pet'),
]





