from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_topic, name='create_topic'),
]