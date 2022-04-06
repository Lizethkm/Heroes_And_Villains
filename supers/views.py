from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super




# Create your views here.
@api_view(['GET','POST'])

def list_supers(request):

    if request.method == 'GET':
        super_type_param= request.query_params.get('type')
        sort_param= request.query_params.get('sort')
        supers= Super.objects.all()

        if super_type_param:
            supers= supers.filter(super_type__type=super_type_param)
            serializer= SuperSerializer(supers, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        if sort_param:
            supers= supers.order_by(sort_param)
            serializer= SuperSerializer(supers, many=True)
            return Response(serializer.data)
        
        serializer= SuperSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer= SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        





@api_view(['GET','PUT','DELETE'])
def retrieve_super(request, pk):
    
    super= get_object_or_404(Super, pk=pk)

    if request.method == 'GET':
        serializer= SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer= SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    

