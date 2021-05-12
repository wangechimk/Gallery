from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('landing/', views.homepage, name='landing'), 
    path('gallery', views.gallery, name='gallery')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 