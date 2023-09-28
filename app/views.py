from django.http import JsonResponse
from .models import Shop
from .serializers import shop_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])

def shop_items(request):
    if request.method == "GET":
        shop_obj = Shop.objects.all()
        serializer =shop_serializer(shop_obj, many=True)
        return JsonResponse({'shop': serializer.data})
    
    if request.method == 'POST':
        serializer = shop_serializer(data=request.data)
        if serializer.is_valid():
            serializer.szve()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

 