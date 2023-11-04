from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_home, name = "home"),
    
]