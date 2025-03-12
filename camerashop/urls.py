from django.urls import path, include
from rest_framework.routers import DefaultRouter

from camerashop import views

r = DefaultRouter()
r.register('users', views.UserViewSet, basename='user')
r.register('categories', views.CategoryViewSet, basename='category')
r.register('subcategories', views.SubCategoryViewSet, basename='subcategory')
r.register('manufacturers', views.ManufacturerViewSet, basename='manufacturer')
r.register('products', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(r.urls)),
]