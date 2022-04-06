from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super

# Create your views here.
@api_view(['GET','POST'])

def list_supers(request):

    if request.method == 'POST':
        serializer= SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':

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

        super_types= SuperType.objects.all()
        
        custom_response_dictionary= {}

        for super_type in super_types:

            super_types= supers.filter(super_type_id= super_type.id)

            serializer= SuperSerializer(super_types, many=True)

            custom_response_dictionary[super_type.type] = {
                'super_type': super_type.type,
                'supers': serializer.data
            }
        return Response(custom_response_dictionary)


        
    serializer= SuperSerializer(supers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

     

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






    

