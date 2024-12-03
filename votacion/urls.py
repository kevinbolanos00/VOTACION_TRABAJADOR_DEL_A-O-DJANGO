from django.urls import path
from . import views
from .views import votar
#app_name = 'votacion' 
urlpatterns = [
     #path('votar/', votar, name='votar'),
     path('votar/', views.votar, name='votar'),
]