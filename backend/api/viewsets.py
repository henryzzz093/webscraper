from rest_framework.viewsets import ModelViewSet
from . import models, serializers

class ApartmentsViewSet(ModelViewSet):
    serializer_class = serializers.ApartmentsSerializer
    queryset = models.Apartments.objects.all().order_by("-created_at")


class AirlineViewSet(ModelViewSet):
    serializer_class = serializers.AirlineSerializer
    queryset = models.Airline.objects.all().order_by("-created_at")