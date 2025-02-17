# TeLlevoAPP - API REST

Este proyecto de Django proporciona servicios API REST para la aplicación móvil **TeLlevoApp**, desarrollada en Ionic. Forma parte del trabajo semestral de la asignatura **Programación de Aplicaciones Móviles**, 2023, en la carrera de **Ingeniería en Informática** del Instituto Profesional Duoc UC, sede Antonio Varas.


Repositorio del proyecto en Ionic: [TeLlevoApp](https://github.com/Pablo-Maldonado-Presas/te-llevo-app)

---

## Requisitos previos

### 1. Instalación de Programas
#### Python
- [Descargar Python](https://www.python.org/)

#### MongoDB (motor de base de datos no relacional)
- [Descargar MongoDB Community Edition](https://www.mongodb.com/try/download/community)

#### MongoDB Compass (interfaz gráfica para MongoDB) *(opcional, pero recomendado)*
- [Descargar MongoDB Compass](https://www.mongodb.com/try/download/compass)

---

## Configuración del entorno
### 2. Clonar el repositorio
```cli
 git clone https://github.com/Pablo-Maldonado-Presas/te-llevo-api.git
```

### 3. Crear y activar un entorno virtual
```cli
 python -m venv venv
 source venv/bin/activate  # Para macOS y Linux
 venv\Scripts\activate     # Para Windows
```

### 4. Instalación de dependencias
```cli
 pip install -r requirements.txt
```

*(El archivo ********`requirements.txt`******** incluye todas las dependencias necesarias, evitando la instalación manual de cada paquete.)*

Si necesitas generar o actualizar `requirements.txt`, usa:
```cli
 pip freeze > requirements.txt
```

---

## Configuración y Ejecución del Proyecto
### 5. Configuración de la base de datos
1. Iniciar MongoDB Compass y establecer conexión con el servidor local.
2. Crear una base de datos con el nombre **`api_db`**.

### 6. Aplicar migraciones en Django
```cli
 python manage.py makemigrations
 python manage.py migrate
```
### 7. Poblar la base de datos 
```cli
 python populate_mongodb.py
```

### 8. Ejecutar el servidor de desarrollo
```cli
 python manage.py runserver
```