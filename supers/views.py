from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super




# Create your views here.
@api_view(['GET'])

def list_supers(request):
    
    if request.method == 'GET':
        super=Super.objects.all()
        serializer= SuperSerializer(super, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_heroes(request,fk):
    
    super_type_param= request.query_params.get('type')
    sort_param= request.query_params.get('sort')
    supers= Super.objects.all()

    if super_type_param:
        supers= supers.filter(super_type__type=super_type_param)
        
        serializer= SuperSerializer(heroes, many=True)

    if sort_param:
        heroes= supers.order_by(sort_param)
        heroes=supers.filter(type='Hero')
        serializer= SuperSerializer(heroes, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

    

