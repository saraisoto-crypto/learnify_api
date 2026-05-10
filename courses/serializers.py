from rest_framework import serializers
from .models import Course, Instructor

class InstructorSerializer(serializers.ModelSerializer):
    total_courses = serializers.SerializerMethodField()

    class Meta:
        model = Instructor
        fields = ['id', 'name', 'specialty', 'email', 'total_courses', 'created_at']

    def get_total_courses(self, obj):
        return obj.courses.count()

class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.name', read_only=True)
    instructor_specialty = serializers.CharField(source='instructor.specialty', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'duration', 'level', 'instructor', 'instructor_name', 'instructor_specialty', 'created_at']

class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source='instructor', write_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'duration', 'level', 'instructor', 'instructor_id', 'created_at']