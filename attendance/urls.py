# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('take_attendance/', views.take_attendance, name='take_attendance'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
]
