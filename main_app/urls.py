from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('resources', views.resources, name='resources'),
    path('privacy', views.privacy, name='privacy')
]
