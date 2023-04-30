from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import College
from .serializers import CollegeSerializer

class Colleges(ListAPIView):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()


class CollegeDetails(ListAPIView):      #TODO This should be a details view 
    serializer_class = CollegeSerializer
    queryset = College.objects.all()
