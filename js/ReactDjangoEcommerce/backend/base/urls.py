from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRouters, name="routes"),
    path('products/', views.getProdutcs, name="products"),
    path('products/<str:pk>/', views.getProdutcs, name="products")
]