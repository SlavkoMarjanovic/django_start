from rest_framework import serializers
from .models import RestaurantLocation

class RestaurantLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantLocation
        fields = '__all__'
