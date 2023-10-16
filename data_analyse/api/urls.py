
from django.urls import path
from . import views

urlpatterns = [
    path('send_data/', views.send_data_to_postgresql, name='send_data_to_postgresql'),
]