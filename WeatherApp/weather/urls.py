from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/delete/', views.WeatherDeleteView.as_view(), name='weather_delete'),
]