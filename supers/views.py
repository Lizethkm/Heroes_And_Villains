from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super


# Create your views here.
@api_view(['GET'])

def list_supers(request):
    
    if request.method == 'GET':
        super=Super.objects.all()
        serializer= SuperSerializer(super, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

