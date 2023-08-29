from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer


@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_courses(request):
    videos = Course.objects.all()
    serializer = CourseSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_course_by_id(request,pk):
    try:
        video = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=404)

    serializer = CourseSerializer(video)
    return Response(serializer.data)

@api_view(['PUT'])
def update_course(request, pk):
    try:
        video = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=404)

    serializer = CourseSerializer(video, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_course(request,pk):
    try:
        video = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=404)

    video.delete()
    return Response(status=204)
