from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SuperTypeSerializer
from .models import SuperType


# Create your views here.
@api_view(['GET'])

def list_super_types(request):
    super_type= SuperType.objects.all()
    serializer= SuperTypeSerializer(super_type, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
