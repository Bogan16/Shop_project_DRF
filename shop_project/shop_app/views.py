from .serializers import *
from .models import *
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

class HomeView(APIView):
    
    def get(self, request):
        data = {
            "message": "Welcome to the shop project!",
        }
        return Response(data)

class EntityFilteredList(generics.ListAPIView):
  
    def get_serializer_class(self):
        entity_type = self.request.query_params.get('entity_type')
        if entity_type:
            if entity_type == 'customer':
                return CustomerSerializer
            elif entity_type == 'manager':
                return ManagerSerializer
            elif entity_type == 'delivery_crew':
                return DeliveryCrewSerializer
            elif entity_type == 'cart':
                return CartSerializer
            elif entity_type == 'product':
                return ProductSerializer
        return None

    def get_queryset(self):
        entity_type = self.request.query_params.get('entity_type')
        if entity_type:
            if entity_type == 'customer':
                return Customer.objects.prefetch_related('cart').all()
            elif entity_type == 'manager':
                return Manager.objects.all()
            elif entity_type == 'delivery_crew':
                return DeliveryCrew.objects.all()
            elif entity_type == 'cart':
                return Cart.objects.prefetch_related('items').all()
            elif entity_type == 'product':
                return Product.objects.all()
        return []

class ProductFilteredList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        less_than_price = self.request.query_params.get('lessThan')
        if less_than_price:
            queryset = queryset.filter(price__lt=less_than_price)

        bigger_than_price = self.request.query_params.get('biggerThan')
        if bigger_than_price:
            queryset = queryset.filter(price__gt=bigger_than_price)

        return queryset
    
class ProductSortedList(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']

    def get_queryset(self):
        queryset = Product.objects.all()

        less_than_price = self.request.query_params.get('lessThan')
        if less_than_price:
            queryset = queryset.filter(price__lt=less_than_price)

        bigger_than_price = self.request.query_params.get('biggerThan')
        if bigger_than_price:
            queryset = queryset.filter(price__gt=bigger_than_price)

        return queryset

class EntityProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        entity_type = self.kwargs.get('entity_type')
        if entity_type:
            if entity_type == 'customer':
                entity = Customer.objects.get(pk=self.kwargs['entity_id'])
            elif entity_type == 'manager':
                entity = Manager.objects.get(pk=self.kwargs['entity_id'])
            elif entity_type == 'delivery_crew':
                entity = DeliveryCrew.objects.get(pk=self.kwargs['entity_id'])
            return entity.cart.items.all()
        return []

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DeliveryCrewList(generics.ListCreateAPIView):
    queryset = DeliveryCrew.objects.all()
    serializer_class = DeliveryCrewSerializer

class DeliveryCrewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryCrew.objects.all()
    serializer_class = DeliveryCrewSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['price']

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer