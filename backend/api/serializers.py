from . import models
from rest_framework import serializers


class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apartments
        fields = "__all__"

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Airline
        fields = "__all__"