from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_city, name='search_city'),
    path('detail/<int:city_id>/', views.detail, name='detail'),
]