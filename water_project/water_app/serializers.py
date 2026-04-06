from rest_framework import serializers
from .models import WaterOrder

class WaterOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterOrder
        fields = '__all__'