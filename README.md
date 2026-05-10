# 🎓 Learnify API
API REST para la gestión de cursos online e instructores, desarrollada con Django y Django REST Framework.

## Tecnologías usadas
- Python 3.x
- Django
- Django REST Framework (DRF)
- django-filter
- SQLite (base de datos por defecto)

## Instrucciones para ejecutar el servidor

### 1. Clonar el repositorio
```bash
git clone https://github.com/saraisoto-crypto/learnify_api.git
cd learnify_api
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux/Mac
```

### 3. Instalar dependencias
```bash
pip install django djangorestframework django-filter
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```
La API estará disponible en: `http://127.0.0.1:8000/api/`

---

## Endpoints disponibles

### Instructores (`/api/instructors/`)

#### Listar todos los instructores
```bash
curl -X GET http://127.0.0.1:8000/api/instructors/
```
**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "Ana García",
    "specialty": "Python & Django",
    "email": "ana@learnify.com",
    "total_courses": 2
  }
]
```

#### Crear un instructor
```bash
curl -X POST http://127.0.0.1:8000/api/instructors/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Ana García", "specialty": "Python & Django", "email": "ana@learnify.com"}'
```

#### Editar un instructor
```bash
curl -X PUT http://127.0.0.1:8000/api/instructors/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Ana Actualizada", "specialty": "Django REST", "email": "ana@learnify.com"}'
```

#### Eliminar un instructor
```bash
curl -X DELETE http://127.0.0.1:8000/api/instructors/1/
```

---

### Cursos (`/api/courses/`)

#### Listar todos los cursos
```bash
curl -X GET http://127.0.0.1:8000/api/courses/
```
**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "Django REST Framework",
    "description": "APIs con Django y DRF",
    "duration": 20,
    "level": "beginner",
    "instructor": 1,
    "instructor_name": "Ana García",
    "instructor_specialty": "Python & Django"
  }
]
```

#### Crear un curso
```bash
curl -X POST http://127.0.0.1:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Django REST", "description": "APIs con Django", "duration": 20, "level": "beginner", "instructor_id": 1}'
```

#### Editar un curso
```bash
curl -X PUT http://127.0.0.1:8000/api/courses/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Django Avanzado", "description": "APIs con Django", "duration": 25, "level": "intermediate", "instructor_id": 1}'
```

#### Eliminar un curso
```bash
curl -X DELETE http://127.0.0.1:8000/api/courses/1/
```

#### Buscar cursos
```bash
curl -X GET "http://127.0.0.1:8000/api/courses/?search=Python"
curl -X GET "http://127.0.0.1:8000/api/courses/?search=beginner"
```

---

## Relación entre entidades
Cada curso está asociado a un instructor mediante una ForeignKey.
El campo `instructor_name` e `instructor_specialty` se muestran directamente en la respuesta del curso.

---

## Estructura del proyecto
```
learnify_api/
├── learnify_api/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── seed_data.py
└── manage.py
```