from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Degree
from .serializers import DegreeSerializer

@api_view(['POST'])
def create_degree(request):
    serializer = DegreeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_degrees(request):
    degrees = Degree.objects.all()
    serializer = DegreeSerializer(degrees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_degree(request, degree_id):
    try:
        degree = Degree.objects.get(pk=degree_id)
    except Degree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = DegreeSerializer(degree)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_degree(request, degree_id):
    try:
        degree = Degree.objects.get(pk=degree_id)
    except Degree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    degree.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_degree(request, degree_id):
    try:
        degree = Degree.objects.get(pk=degree_id)
    except Degree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = DegreeSerializer(degree, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
