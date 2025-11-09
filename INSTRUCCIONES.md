# 📝 Instrucciones de Instalación y Ejecución

## 🔧 Paso 1: Instalar Python y pip (si no lo tienes)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

## 📦 Paso 2: Crear entorno virtual (recomendado)

```bash
cd "/home/hazling/Escritorio/Juegos Lorena"
python3 -m venv venv
source venv/bin/activate
```

## 📥 Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🎨 Paso 4: Generar códigos QR

```bash
python3 generate_qr.py
```

Esto creará los códigos QR en la carpeta `static/qr/`

## 🚀 Paso 5: Ejecutar la aplicación localmente

```bash
python3 app.py
```

Luego abre tu navegador en: `http://localhost:5000`

## 📱 Paso 6: Probar en tu celular (misma red WiFi)

1. Encuentra tu IP local:
```bash
hostname -I
```

2. En tu celular, abre el navegador y ve a:
```
http://TU_IP_LOCAL:5000
```

Por ejemplo: `http://192.168.1.100:5000`

---

## 🌐 Despliegue en Servidor Gratuito

### Opción 1: Render.com (Recomendado - Más fácil)

1. **Crear cuenta en Render.com**
   - Ve a https://render.com
   - Regístrate con GitHub

2. **Subir código a GitHub**
   ```bash
   cd "/home/hazling/Escritorio/Juegos Lorena"
   git init
   git add .
   git commit -m "Juegos educativos del abecedario"
   ```
   
   Luego crea un repositorio en GitHub y súbelo:
   ```bash
   git remote add origin https://github.com/TU_USUARIO/juegos-abecedario.git
   git push -u origin main
   ```

3. **Crear Web Service en Render**
   - En Render, click en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Configuración:
     - **Name**: juegos-abecedario
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click "Create Web Service"

4. **Actualizar códigos QR con URL real**
   - Render te dará una URL como: `https://juegos-abecedario.onrender.com`
   - Edita `generate_qr.py` y cambia:
     ```python
     BASE_URL = "https://juegos-abecedario.onrender.com"
     ```
   - Regenera los QR:
     ```bash
     python3 generate_qr.py
     ```
   - Haz commit y push:
     ```bash
     git add static/qr/
     git commit -m "Actualizar QR codes con URL de producción"
     git push
     ```

### Opción 2: Railway.app

1. **Crear cuenta en Railway**
   - Ve a https://railway.app
   - Regístrate con GitHub

2. **Subir código a GitHub** (igual que arriba)

3. **Desplegar en Railway**
   - En Railway, click "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Elige tu repositorio
   - Railway detectará automáticamente que es Flask
   - Espera a que se despliegue

4. **Obtener URL y actualizar QR codes**
   - Railway te dará una URL
   - Actualiza `generate_qr.py` con esa URL
   - Regenera QR codes y haz push

### Opción 3: PythonAnywhere (Más manual)

1. **Crear cuenta gratuita**
   - Ve a https://www.pythonanywhere.com
   - Crea cuenta gratuita

2. **Subir archivos**
   - Usa la interfaz web para subir todos los archivos
   - O usa Git para clonar tu repositorio

3. **Configurar Web App**
   - En el dashboard, ve a "Web"
   - Click "Add a new web app"
   - Elige Flask
   - Configura el WSGI file para apuntar a tu `app.py`

4. **Actualizar QR codes**
   - Tu URL será: `https://TU_USUARIO.pythonanywhere.com`
   - Actualiza `generate_qr.py` y regenera los QR

---

## 🖨️ Imprimir Códigos QR

Los códigos QR están en: `static/qr/`

Puedes:
1. Imprimirlos individualmente
2. Crear un PDF con todos los QR codes
3. Pegarlos en tarjetas o carteles para tu presentación

### Crear PDF con todos los QR (opcional)

Instala reportlab:
```bash
pip install reportlab
```

Ejecuta el script de generación de PDF:
```bash
python3 create_qr_pdf.py
```

---

## 🎓 Para tu Presentación Universitaria

### Materiales sugeridos:

1. **Carteles con QR codes**
   - Imprime cada letra del abecedario en grande
   - Pega el QR code correspondiente debajo
   - Los niños pueden escanear con tablet o celular

2. **Demostración en vivo**
   - Proyecta la página principal
   - Muestra 2-3 juegos en acción
   - Explica la interactividad táctil

3. **Documentación técnica**
   - Muestra el código
   - Explica la arquitectura (Flask + HTML5 Canvas)
   - Menciona la accesibilidad móvil

### Puntos clave para tu presentación:

- ✅ 27 juegos interactivos (A-Z + Ñ)
- ✅ Diseñado para niños de 1-3 años
- ✅ Interfaz táctil optimizada para móviles
- ✅ Códigos QR para acceso rápido
- ✅ 100% Python (Flask backend)
- ✅ HTML5 Canvas para gráficos
- ✅ Responsive design
- ✅ Desplegado en servidor gratuito
- ✅ Educativo y entretenido

---

## 🐛 Solución de Problemas

### Error: "Address already in use"
```bash
# Mata el proceso que usa el puerto 5000
sudo lsof -t -i:5000 | xargs kill -9
```

### Los QR codes no funcionan
- Verifica que la URL en `generate_qr.py` sea correcta
- Regenera los QR codes después de cambiar la URL
- Asegúrate de que el servidor esté corriendo

### El juego no se ve bien en móvil
- Verifica que el viewport esté configurado
- Prueba en modo incógnito (sin caché)
- Limpia la caché del navegador

---

## 📞 Contacto y Soporte

Si tienes problemas, revisa:
1. Los logs del servidor
2. La consola del navegador (F12)
3. Que todas las dependencias estén instaladas

¡Buena suerte con tu presentación! 🎉
