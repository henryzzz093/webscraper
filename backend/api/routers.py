from rest_framework.routers import SimpleRouter

from . import viewsets

routes = SimpleRouter()

routes.register(r"apartment", viewsets.ApartmentsViewSet)
routes.register(r"airline", viewsets.AirlineViewSet)

urlpatterns = [*routes.urls]
