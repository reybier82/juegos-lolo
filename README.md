# 🎮 Juegos Educativos del Abecedario

Proyecto educativo interactivo para niños de preescolar (1-3 años) con juegos para cada letra del abecedario español.

## 📋 Características

- 26 juegos interactivos (A-Z)
- Interfaz táctil optimizada para móviles
- Códigos QR individuales para cada letra
- Diseño colorido y atractivo para niños
- 100% responsive

## 🚀 Instalación Local

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Generar códigos QR:
```bash
python generate_qr.py
```

3. Ejecutar la aplicación:
```bash
python app.py
```

4. Abrir en el navegador: `http://localhost:5000`

## 📱 Despliegue en Servidor Gratuito

### Opción 1: Render.com (Recomendado)

1. Crear cuenta en [Render.com](https://render.com)
2. Conectar tu repositorio de GitHub
3. Crear un nuevo "Web Service"
4. Configurar:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Actualizar `BASE_URL` en `generate_qr.py` con tu URL de Render
6. Regenerar códigos QR y hacer commit

### Opción 2: Railway.app

1. Crear cuenta en [Railway.app](https://railway.app)
2. Conectar repositorio de GitHub
3. Railway detectará automáticamente Flask
4. Actualizar `BASE_URL` en `generate_qr.py`
5. Regenerar códigos QR

### Opción 3: PythonAnywhere

1. Crear cuenta gratuita en [PythonAnywhere](https://www.pythonanywhere.com)
2. Subir archivos via web interface
3. Configurar WSGI file
4. Actualizar `BASE_URL` y regenerar QR codes

## 📂 Estructura del Proyecto

```
Juegos Lorena/
├── app.py                 # Aplicación Flask principal
├── generate_qr.py         # Generador de códigos QR
├── requirements.txt       # Dependencias Python
├── README.md             # Este archivo
├── static/               # Archivos estáticos
│   ├── css/
│   ├── js/
│   ├── images/
│   └── qr/              # Códigos QR generados
└── templates/           # Plantillas HTML
    ├── index.html       # Página principal
    ├── base.html        # Plantilla base
    └── juegos/          # Juegos individuales
        ├── A.html
        ├── B.html
        └── ...
```

## 🎨 Juegos Incluidos

- **A** - Aplastar Burbujas
- **B** - Buscar Objetos
- **C** - Colorear
- **D** - Dibujar
- **E** - Explotar Globos
- **F** - Flores Mágicas
- **G** - Girar
- **H** - Hacer Música
- **I** - Iluminar Estrellas
- **J** - Jabón y Burbujas
- **K** - Karaoke
- **L** - Laberinto
- **M** - Mover Animales
- **N** - Números
- **O** - Ordenar Círculos
- **P** - Pintar
- **Q** - Queso para Ratón
- **R** - Rompecabezas
- **S** - Sonidos
- **T** - Tambor
- **U** - Uvas para Contar
- **V** - Volar Mariposas
- **W** - Waffles
- **X** - Xilófono
- **Y** - Yo-yo
- **Z** - Zoológico

## 🔧 Tecnologías

- Python 3.8+
- Flask 3.0
- HTML5 Canvas
- CSS3
- JavaScript (Vanilla)
- QR Code Generator

## 📄 Licencia

Proyecto educativo - Uso libre para fines educativos

## 👨‍💻 Autor

Proyecto para presentación universitaria
# juegos-lolo
