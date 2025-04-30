from rest_framework import serializers
from home.models import NutritionMetrics

class NutritionMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionMetrics
        fields = ['id', 'foodname', 'calories', 'carbs', 'fat', 'sugar', 'protein']

