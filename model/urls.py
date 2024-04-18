from django.urls import path
from . import views

urlpatterns = [
    path('predict_from_csv/', views.predict_from_csv, name='predict_from_csv'),
    path('', views.home),
]