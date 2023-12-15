from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .models import Course
from .serializer import CourseSerializer, CourseDetailSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsInstructorOrReadOnly, IsStudantOrInstructor
from rest_framework.permissions import IsAuthenticated


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInstructorOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(students=self.request.user)


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStudantOrInstructor]

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_url_kwarg = "course_id"

