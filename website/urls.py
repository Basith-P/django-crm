from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('add/', views.add_record, name='add-record'),
    path('delete-record/<int:pk>/', views.delete_record, name='delete-record'),
    path('update-record/<int:pk>/', views.update_record, name='update-record'),
]
