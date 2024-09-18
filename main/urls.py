from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/', CarsAPIView.as_view()),
    path('api/v1/cars/<int:id>/', CarDetailView.as_view(), name='car-detail'),
]
