from rest_framework import serializers
from .models import Customer, Manager, Product, Cart, DeliveryCrew

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Customer
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class DeliveryCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCrew
        fields = '__all__'