from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course, Instructor
from .serializers import CourseSerializer, InstructorSerializer, CourseDetailSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'specialty']

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('instructor').all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'level']
    filterset_fields = ['level', 'instructor']

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update', 'partial_update']:
            return CourseDetailSerializer
        return CourseSerializer