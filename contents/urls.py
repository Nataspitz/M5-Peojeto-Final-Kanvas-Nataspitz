from django.urls import path
from . import views


urlpatterns = [
    path("courses/<uuid:course_id>/contents/", views.CourseContentView.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:content_id>/", views.CourseContentDetailView.as_view()),
]