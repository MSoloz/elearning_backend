from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_subject, name='create_subject'),
    path('all/', views.get_all_subjects, name='get_all_subjects'),
    path('<int:subject_id>/', views.get_subject, name='get_subject'),
    path('<int:subject_id>/delete/', views.delete_subject, name='delete_subject'),
    path('<int:subject_id>/update/', views.update_subject, name='update_subject'),
]
