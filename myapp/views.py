from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status


#my imports
from .serilalizers import ProductSerializer, SaleSerializer, PaySerializer
from users.models import User
from .models import Product
# Create your views here.

class ProductCreateList(APIView):

    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user = User.objects.filter(id = payload['id']).first()
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save(user=user)
        
        return Response(serializer.data)
    
    def get(self, request):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(serializer.data)
    

class ProductGetDelete(APIView):

    def get(self, request, pk):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        products = Product.objects.get(pk = pk)
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)
    
    def post(self, request, pk):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            product = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"msg": "Delete Sucess!"})

        




