from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.frontend, name='map_page'),  # Default view
]
