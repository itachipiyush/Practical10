from django.urls import path
from data10 import views

app_name = 'data10'

urlpatterns = [
    path('Add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('display/', views.display, name='display'),
    path('', views.display, name='display'),
]
