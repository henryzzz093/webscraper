from rest_framework.routers import SimpleRouter

from . import viewsets

routes = SimpleRouter()

routes.register(r"apartments", viewsets.ApartmentsViewSet)

urlpatterns = [*routes.urls]
