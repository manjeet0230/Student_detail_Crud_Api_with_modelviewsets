from django.shortcuts import render
from .models import studentmodel
from .serializers import Studentsrializer
from rest_framework import viewsets

class modelviewsets(viewsets.ModelViewSet):
    queryset=studentmodel.objects.all()
    serializer_class=Studentsrializer


