from django.urls import path
from . import views


urlpatterns = [
   path('generate/', views.generate_question, name='generate_video'),
] 