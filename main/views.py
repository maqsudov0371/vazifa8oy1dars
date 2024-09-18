from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import CarsSerializer

# Create your views here.

class CarsAPIView(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class CarDetailView(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    lookup_field = 'id'