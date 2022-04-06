from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super
from supers import serializers




# Create your views here.
@api_view(['GET'])

def list_supers(request):
    
    super_type_param= request.query_params.get('type')
    sort_param= request.query_params.get('sort')
    supers= Super.objects.all()

    if super_type_param:
        supers= supers.filter(super_type__type=super_type_param)
        serializer= SuperSerializer(supers, many=True)
        return Response(serializer.data)

    if sort_param:
        supers= supers.order_by(sort_param)
        serializer= SuperSerializer(supers, many=True)
        return Response(serializer.data)
    
    serializer= SuperSerializer(supers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def retrieve_super(request, pk):
    
    super= get_object_or_404(Super, pk=pk)

    if request.method == 'GET':
        serializer= SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

