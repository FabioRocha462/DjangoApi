from rest_framework import serializers

#my imports

from .models import Product, Sale, Pay

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['id', 'name','quantity', 'validity', 'user', 'bidding_value', 'category','created_at','updated_at']
class SaleSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ['id', 'product', 'user', 'quantity','created_at']

class PaySerializer(serializers.ModelSerializer):

    class Meta:

        fields = ['id', 'value', 'user', 'created_at']