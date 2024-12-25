from rest_framework import serializers
from .models import Statistics

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['id', 'date', 'visitors_count', 'revenue', 'event_count']