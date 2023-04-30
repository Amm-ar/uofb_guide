from rest_framework.serializers import ModelSerializer
from .models import College

class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
        
    