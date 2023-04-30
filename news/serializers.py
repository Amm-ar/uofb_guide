from .models import Article, Anouncement
from rest_framework.serializers import ModelSerializer

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__' 


class AnouncementSerializer(ModelSerializer):
    class Meta:
        model = Anouncement
        fields = '__all__' 
