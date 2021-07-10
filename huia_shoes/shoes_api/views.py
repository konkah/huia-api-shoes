from .models import Batch, Product, Client, Order
from .serializers import BatchSerializer, ProductSerializer, ClientSerializer, OrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer