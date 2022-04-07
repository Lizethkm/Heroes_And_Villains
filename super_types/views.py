from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SuperTypeSerializer
from .models import SuperType


# Create your views here.
@api_view(['GET','POST'])

def list_super_types(request):

    if request.method == 'GET':
        super_type= SuperType.objects.all()
        serializer= SuperTypeSerializer(super_type, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer= SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])

def super_type_details(request,pk):

    super_type= get_object_or_404(SuperType, pk=pk)
    serializer= SuperTypeSerializer(super_type)
    return Response(serializer.data, status=status.HTTP_200_OK)
