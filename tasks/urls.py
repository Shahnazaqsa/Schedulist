from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name = 'add'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('edit/<int:task_id>/' , views.edit , name = 'edit')
]
