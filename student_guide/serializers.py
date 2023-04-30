from rest_framework.serializers import ModelSerializer
from .models import GuideEntry

class GuideEntrySerializer(ModelSerializer):
    class Meta:
        model = GuideEntry
        fields = '__all__'
        