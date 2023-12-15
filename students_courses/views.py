from rest_framework.generics import RetrieveUpdateAPIView
from courses.models import Course
from courses.serializer import CourseRegisterSerializer


class StudentCourseView(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRegisterSerializer
    lookup_url_kwarg = "course_id"
