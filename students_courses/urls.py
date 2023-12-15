from django.urls import path
from . import views


urlpatterns = [
    path("courses/<uuid:course_id>/students/", views.StudentCourseView.as_view()),
]