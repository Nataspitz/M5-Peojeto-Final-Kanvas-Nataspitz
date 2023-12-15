from rest_framework import serializers
from .models import Course
from accounts.serializer import AccountSerializer
from students_courses.serializer import StudentCourseSerializer
from contents.serializer import ContentSerializer
from accounts.models import Account


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "name", "status", "start_date", "end_date", "instructor", "students_courses", "contents"] 
        extra_kwargs = {
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }


class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = AccountSerializer(read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "status", "start_date", "end_date", "instructor", "students_courses", "contents"] 


class CourseRegisterSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses" ]
        depth = 1
        extra_kwargs = {
            "name": {"read_only": True},
        }

    def update(self, instance, validated_data):
        found_students = []
        dont_students = []

        for student_course in validated_data["students_courses"]:
            student = student_course["student"]

            account = Account.objects.filter(email=student["email"]).first()
            if not account:
                dont_students.append(student["email"])
            else: 
                found_students.append(account)

        if dont_students:
            email_string = ", ".join(dont_students)
            raise serializers.ValidationError({
	            "detail": f"No active accounts was found: {email_string}."
            })

        if not self.partial:
            instance.students.add(*found_students) 
            return instance
        
        return super().update(instance, validated_data)

