from rest_framework import serializers
from recognize_videos.models import RecognizeVideo

class RecognizeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognizeVideo
        fields = ('id', 'title')