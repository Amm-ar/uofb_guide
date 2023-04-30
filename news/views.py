from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article, Anouncement
from .serializers import ArticleSerializer, AnouncementSerializer

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    

class AnouncementViewSet(ModelViewSet):
    serializer_class = AnouncementSerializer
    queryset = Anouncement.objects.all()
    
