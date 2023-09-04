from rest_framework import viewsets, serializers
import django_filters.rest_framework

from retail_network.models import Entrepreneur, Retailer, Factory
from retail_network.permissions import IsActiveEmployee
from retail_network.serializers import EntrepreneurSerializer, RetailerSerializer, FactorySerializer

def prohibiting_updates_from_API(request, *args, **kwargs):
    data = request.data
    for field in data:
        if field == "arrears":
            raise serializers.ValidationError({"arrears": "Нельзя обновлять задолженность через API"})


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ("contacts__country",)

    def list(self, request, *args, **kwargs):
        country = request.GET.get('country', None)
        if country:
            self.queryset = self.queryset.filter(contacts__country=country)
        return super().list(request, *args, **kwargs)

    def update(self, request, pk=None):
        prohibiting_updates_from_API(request, pk)
        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        prohibiting_updates_from_API(request, pk)
        return super().partial_update(request, pk)


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ("contacts__country",)

    def list(self, request, *args, **kwargs):
        country = request.GET.get('country', None)
        if country:
            self.queryset = self.queryset.filter(contacts__country=country)
        return super().list(request, *args, **kwargs)

    def update(self, request, pk=None):
        prohibiting_updates_from_API(request, pk)
        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        prohibiting_updates_from_API(request, pk)
        return super().partial_update(request, pk)




class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ("contacts__country",)

    def list(self, request, *args, **kwargs):
        country = request.GET.get('country', None)
        if country:
            self.queryset = self.queryset.filter(contacts__country=country)
        return super().list(request, *args, **kwargs)

    def update(self, request, pk=None):
        prohibiting_updates_from_API(request, pk)
        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        prohibiting_updates_from_API(request, pk)
        return super().partial_update(request, pk)
