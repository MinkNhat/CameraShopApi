import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from oauth2_provider.views import TokenView
from rest_framework import viewsets, generics, parsers, permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from camerashop import serializers
from camerashop.models import *


class CustomTokenView(TokenView):
    def post(self, request, *args, **kwargs):
        body_data = json.loads(request.body)
        username = body_data.get('username')
        password = body_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return JsonResponse({
                "error": "invalid_grant",
                "error_description": "Tên đăng nhập hoặc mật khẩu không chính xác!"
            }, status=400)

        return super().post(request, *args, **kwargs)


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    @action(methods=['get', 'patch'], url_path='current-user', detail=False, permission_classes=[permissions.IsAuthenticated])
    def get_user(self, request):
        u = request.user
        if request.method.__eq__('PATCH'):
            for key, value in request.data.items():
                if key.__eq__('password'):
                    u.set_password(value)
                else:
                    setattr(u, key, value)
            u.save()
        return Response(serializers.UserSerializer(u, context={'request': request}).data)


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = serializers.CategorySerializer


class ProductViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Product.objects.filter(active=True)
    serializer_class = serializers.ProductSerializer
