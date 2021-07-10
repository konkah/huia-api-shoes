from rest_framework import serializers
from .models import Batch, Product, Client, Order
from validate_docbr import CPF


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = [
            'id',
            'identifier_code',
            'manufacturing_date',
            'product_qty',
        ]
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'identifier_code',
            'name',
            'batch_number',
            'colour',
            'description',
            'value',
        ]
    
    
class ClientSerializer(serializers.ModelSerializer):
    def to_representation(self, data):
        data = super(ClientSerializer, self).to_representation(data)
        data['cpf'] = data['cpf'][0:3] + '.' + data['cpf'][3:6] + '.' + data['cpf'][6:9] + '-' + data['cpf'][9:11]
        return data

    def to_internal_value(self, data):
        data = super(ClientSerializer, self).to_internal_value(data)
        data['cpf'] = data['cpf'].replace('.', '').replace('-', '')
        return data

    class Meta:
        model = Client
        fields = [
            'id',
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

    def set_cpf(self, obj, value):
        obj.cpf = 'value'
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'client',
            'order_date',
            'seller',
            'products',
            'total_value',
        ]

class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'client',
            'order_date',
            'seller',
            'products',
            'total_value',
        ]
        depth = 1