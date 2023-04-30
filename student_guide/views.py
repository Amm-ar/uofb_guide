from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import GuideEntry
from .serializers import GuideEntrySerializer

class GuideViewSet(ModelViewSet):
    serializer_class = GuideEntrySerializer
    queryset = GuideEntry.objects.all()
    authentication_classes = []
    
