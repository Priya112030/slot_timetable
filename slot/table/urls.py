from django.urls import path
from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('view1/', views.view1, name='view1'),
    
]