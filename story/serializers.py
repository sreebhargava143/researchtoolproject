from .models import Storyline
from rest_framework import serializers

class StorylineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storyline
        fields = '__all__'
