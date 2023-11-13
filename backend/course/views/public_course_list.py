from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from course.models import Course
from course.serializers.public_course_list import PublicCourseListSerializer

class PublicCourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.filter(is_public=True)
    serializer_class = PublicCourseListSerializer