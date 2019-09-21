practica2_grupo9

## Pre Requirements
*Install Crypy
```pip install django-crispy-forms```

* Comando para iniciar aplicacion
 ```python manage.py runserver```

 * Comando para correr coverage y errores
 ```coverage run --source='.' manage.py test ClinicaMedica```

 * Comando para ver reporte de coverage
 ```coverage report -m```

* Comando para detectar cambios en nuestros modelos
```python manage.py makemigrations```

* Comando para realizar los cambios
```python manage.py migrate```