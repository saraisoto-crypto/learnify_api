import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnify_api.settings')
django.setup()

from courses.models import Instructor, Course

Course.objects.all().delete()
Instructor.objects.all().delete()

instructors = [
    Instructor.objects.create(name="Ana García", specialty="Python & Django", email="ana@learnify.com"),
    Instructor.objects.create(name="Carlos Mendoza", specialty="JavaScript & React", email="carlos@learnify.com"),
    Instructor.objects.create(name="María López", specialty="Data Science", email="maria@learnify.com"),
]

courses = [
    Course.objects.create(name="Django REST Framework", description="APIs con Django y DRF", duration=20, level="beginner", instructor=instructors[0]),
    Course.objects.create(name="Python Avanzado", description="Decoradores y async", duration=30, level="advanced", instructor=instructors[0]),
    Course.objects.create(name="React con TypeScript", description="Apps modernas con React", duration=25, level="intermediate", instructor=instructors[1]),
    Course.objects.create(name="Machine Learning", description="ML con scikit-learn", duration=40, level="intermediate", instructor=instructors[2]),
]

print("✅ Datos cargados!")
print(f"   - {len(instructors)} instructores")
print(f"   - {len(courses)} cursos")