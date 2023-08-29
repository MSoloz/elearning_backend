from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_degree, name='create_degree'),
    path('all/', views.get_all_degrees, name='get_all_degrees'),
    path('<int:degree_id>/', views.get_degree, name='get_degree'),
    path('<int:degree_id>/delete/', views.delete_degree, name='delete_degree'),
    path('<int:degree_id>/update/', views.update_degree, name='update_degree'),
]
