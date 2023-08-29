from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/question/',include('question.urls')),
    path('api/course/',include('course.urls')),
    path('api/subject/',include('subject.urls')),
    path('api/',include('user.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
