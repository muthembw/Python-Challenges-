from django.urls import path
from .views import home

#URL CONFIGURATION
urlpatterns = [
    path('hello/', home)
]