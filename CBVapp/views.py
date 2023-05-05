from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Course, CourseSerializer
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class PriceUpdateViewSet(APIView):
    def post(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

        newCourse = Course(id=course.id, name=course.name, author=course.author,
                           price=request.data['price'],
                           discount=course.discount,
                           duration=course.discount)

        newCourse.save()
        serializer = CourseSerializer(newCourse)
        return Response(serializer.data)


# class CourseListView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         courseSerializer = CourseSerializer(data=request.data)
#         if courseSerializer.is_valid():
#             courseSerializer.save()
#             return Response(courseSerializer.data, status=status.HTTP_201_CREATED)

#         return Response(courseSerializer.errors)


# class CourseDetailView(APIView):
#     def get_course(self, pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         course = self.get_course(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         course = self.get_course(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, pk):
#         course = self.get_course(pk)
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
