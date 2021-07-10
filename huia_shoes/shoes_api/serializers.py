from rest_framework import serializers
from .models import Batch, Product, Client, Order
from validate_docbr import CPF


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = [
            'identifier_code',
            'manufacturing_date',
            'product_qty',
        ]
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'identifier_code',
            'name',
            'batch_number',
            'colour',
            'description',
            'value',
        ]
    
    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'name',
            'cpf',
            'birth_date',
        ]
    
    def validate_cpf(self, value):
        cpf = CPF()
        if not cpf.validate(value):
            raise serializers.ValidationError(
                'Não é um CPF válido!'
            )
        return value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'order_number',
            'client',
            'seller',
            'products',
            'total_value',
        ]