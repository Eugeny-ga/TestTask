
from rest_framework import routers

from retail_network.views import FactoryViewSet, RetailerViewSet, EntrepreneurViewSet
router = routers.DefaultRouter()
router.register(r'factory', FactoryViewSet)
router.register(r'retailer', RetailerViewSet)
router.register(r'entrepreneur', EntrepreneurViewSet)
