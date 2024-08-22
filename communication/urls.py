# urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),
   path('inbox/', views.inbox, name='inbox'),
]
