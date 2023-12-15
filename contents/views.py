from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Content
from .serializer import ContentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsIntructor, IsInstrutorOrReadOnlyContent
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from courses.models import Course


class CourseContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsIntructor]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        serializer.save(course_id=self.kwargs["course_id"])

class CourseContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInstrutorOrReadOnlyContent]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def get_object(self):
        try:
            course_id = self.kwargs['course_id']
            content_id = self.kwargs['content_id']

            Course.objects.get(id=course_id)
            content = Content.objects.get(id=content_id)
        
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        
        self.check_object_permissions(self.request, content)
        return content
    


    
