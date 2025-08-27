"""django_tasklist URL Configuration
...
"""
from django.contrib import admin
from django.urls import path

from mc_tasklist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Trailing slash and a unique name were added
    path('add/', views.add, name='add_task'),
    
    # Trailing slash and a unique name were added
    path('remove/', views.remove, name='remove_task'),
    
    # A unique name was added
    path('', views.index, name='task_list'),
]
