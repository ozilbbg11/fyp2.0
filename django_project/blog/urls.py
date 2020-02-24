from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('generate/', views.generate, name='blog-generate'),
    path('trend/', views.trend, name='blog-trend'),
]
