from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_topic, name='create_topic'),
    path('all/', views.get_all_topics, name='get_all_topics'),
    path('<int:topic_id>/', views.get_topic, name='get_topic'),
    path('<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
    path('<int:topic_id>/update/', views.update_topic, name='update_topic'),
    path('by_degree/<str:degree>/', views.get_topic_by_degree, name='get_topic_by_degree'),
    path('by_subject/<str:subject>/', views.get_topic_by_subject, name='get_topic_by_subject'),
    path('by_degree_and_subject/<str:degree>/<str:subject>/', views.get_topic_by_degree_and_subject, name='get_topic_by_degree_and_subject'),
]