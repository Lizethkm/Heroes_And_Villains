from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers


# Create your views here.
@api_view(['GET'])

def list_supers(request):
    
    if request.method == 'GET':
        super=Supers.objects.all()
        serializer= SupersSerializer(super, many=True)
        return Response(serializer.data)

    

