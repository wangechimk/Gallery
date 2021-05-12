from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='picha'
urlpatterns=[
    path('', views.homepage, name='landing'), 
    path('gallery/', views.gallery, name='gallery')
]
