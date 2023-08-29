from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('update/<int:pk>/', views.update_course, name='update_course'),
    path('all/', views.get_all_courses, name='get_all_course'),
    path('<int:pk>/', views.get_course_by_id, name='get_course_by_id'),
    path('delete/<int:pk>/', views.delete_course, name='delete_course'),
]