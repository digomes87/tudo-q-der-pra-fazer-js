from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products


@api_view(['GET'])
def getRouters(request):
    routes = [
        'asdadas/api',
        'asdad/12',
        '1232/123/12'
    ]
    return Response(routes)

@api_view(['GET'])
def getProdutcs(request):
    return Response(products)

@api_view(['GET'])
def getProdutcs(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break
        
    return Response(products)

