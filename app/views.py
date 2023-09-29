from django.http import JsonResponse
from .models import Shop
from .serializers import shop_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def shop_items(request, format = None):
    if request.method == 'GET':
        shop_obj = Shop.objects.all()
        serializer = shop_serializer(shop_obj, many=True)
        return Response({'shop': serializer.data})
    
    if request.method == 'POST':
        serializer = shop_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def shop_items_details(request, id, format = None):
    try:
        Shop_obj = Shop.objects.get(pk=id)
    except Shop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = shop_serializer(Shop_obj)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = shop_serializer(Shop_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Shop_obj.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
