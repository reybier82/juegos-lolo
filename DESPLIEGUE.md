# 🚀 Guía Completa de Despliegue

## Servidores Gratuitos Recomendados

### 🥇 Render.com (MÁS RECOMENDADO)
**Ventajas:**
- ✅ Completamente gratuito
- ✅ Muy fácil de usar
- ✅ SSL automático (HTTPS)
- ✅ Despliegue automático desde GitHub
- ✅ No requiere tarjeta de crédito

**Pasos detallados:**

1. **Preparar el repositorio Git**
   ```bash
   cd "/home/hazling/Escritorio/Juegos Lorena"
   git init
   git add .
   git commit -m "Initial commit: Juegos educativos del abecedario"
   ```

2. **Crear repositorio en GitHub**
   - Ve a https://github.com/new
   - Nombre: `juegos-abecedario-preescolar`
   - Público o Privado (tu elección)
   - NO inicialices con README
   - Crea el repositorio

3. **Subir código a GitHub**
   ```bash
   git remote add origin https://github.com/TU_USUARIO/juegos-abecedario-preescolar.git
   git branch -M main
   git push -u origin main
   ```

4. **Crear cuenta en Render**
   - Ve a https://render.com
   - Click en "Get Started for Free"
   - Regístrate con GitHub (más fácil)

5. **Crear Web Service**
   - En el dashboard, click "New +"
   - Selecciona "Web Service"
   - Conecta tu repositorio de GitHub
   - Configuración:
     ```
     Name: juegos-abecedario
     Region: Oregon (US West) o el más cercano
     Branch: main
     Runtime: Python 3
     Build Command: pip install -r requirements.txt
     Start Command: gunicorn app:app
     ```
   - Plan: Free
   - Click "Create Web Service"

6. **Esperar el despliegue**
   - Render instalará las dependencias
   - Iniciará la aplicación
   - Te dará una URL como: `https://juegos-abecedario.onrender.com`

7. **Actualizar códigos QR**
   - Edita `generate_qr.py`:
     ```python
     BASE_URL = "https://juegos-abecedario.onrender.com"
     ```
   - Regenera los QR localmente:
     ```bash
     python3 generate_qr.py
     ```
   - Sube los cambios:
     ```bash
     git add static/qr/
     git add generate_qr.py
     git commit -m "Actualizar QR codes con URL de producción"
     git push
     ```
   - Render se redespliegará automáticamente

---

### 🥈 Railway.app (Alternativa Excelente)

**Ventajas:**
- ✅ Muy fácil de usar
- ✅ $5 de crédito gratis al mes
- ✅ Despliegue automático
- ✅ SSL automático

**Pasos:**

1. **Preparar Git** (igual que Render)

2. **Crear cuenta en Railway**
   - Ve a https://railway.app
   - Regístrate con GitHub

3. **Nuevo proyecto**
   - Click "New Project"
   - "Deploy from GitHub repo"
   - Selecciona tu repositorio
   - Railway detectará automáticamente Flask

4. **Configurar dominio**
   - Ve a Settings
   - Generate Domain
   - Obtendrás una URL como: `https://juegos-abecedario.up.railway.app`

5. **Actualizar QR codes** (igual que Render)

---

### 🥉 PythonAnywhere (Más Manual)

**Ventajas:**
- ✅ Siempre gratuito
- ✅ No se duerme (a diferencia de Render free)
- ✅ Bueno para proyectos educativos

**Desventajas:**
- ⚠️ Configuración más manual
- ⚠️ Límite de tráfico

**Pasos:**

1. **Crear cuenta**
   - Ve a https://www.pythonanywhere.com
   - Crea cuenta gratuita

2. **Subir archivos**
   - Opción A: Usar Git
     ```bash
     git clone https://github.com/TU_USUARIO/juegos-abecedario-preescolar.git
     ```
   - Opción B: Subir archivos manualmente via web

3. **Crear Web App**
   - Dashboard → Web → Add a new web app
   - Python 3.10
   - Flask
   - Ruta: `/home/TU_USUARIO/juegos-abecedario-preescolar`

4. **Configurar WSGI**
   - Edita el archivo WSGI:
     ```python
     import sys
     path = '/home/TU_USUARIO/juegos-abecedario-preescolar'
     if path not in sys.path:
         sys.path.append(path)
     
     from app import app as application
     ```

5. **Instalar dependencias**
   - Abre una consola Bash
   ```bash
   cd juegos-abecedario-preescolar
   pip3 install --user -r requirements.txt
   ```

6. **Reload web app**
   - En la pestaña Web, click "Reload"

7. **Tu URL será:**
   - `https://TU_USUARIO.pythonanywhere.com`

---

### 🎯 Vercel (Bonus - Muy Rápido)

**Nota:** Vercel es principalmente para sitios estáticos, pero funciona con Flask.

1. **Instalar Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Desplegar**
   ```bash
   cd "/home/hazling/Escritorio/Juegos Lorena"
   vercel
   ```

3. **Seguir las instrucciones**
   - Login con GitHub
   - Confirmar configuración
   - Obtendrás una URL instantánea

---

## 📋 Checklist Post-Despliegue

Después de desplegar, verifica:

- [ ] La página principal carga correctamente
- [ ] Todos los juegos funcionan
- [ ] Los estilos CSS se aplican
- [ ] Los juegos son táctiles en móvil
- [ ] Los códigos QR apuntan a la URL correcta
- [ ] Prueba al menos 5 juegos diferentes
- [ ] Prueba en diferentes dispositivos (PC, tablet, móvil)

---

## 🔧 Solución de Problemas Comunes

### Error: "Application failed to start"
- Verifica que `gunicorn` esté en `requirements.txt`
- Verifica que el comando de inicio sea correcto: `gunicorn app:app`

### Los archivos estáticos no cargan
- Verifica que la carpeta `static/` esté en Git
- Verifica las rutas en los templates: `{{ url_for('static', filename='...') }}`

### Los QR codes no funcionan
- Asegúrate de haber actualizado `BASE_URL` en `generate_qr.py`
- Regenera los QR codes
- Haz commit y push de los nuevos QR codes

### El sitio es muy lento
- Render free se "duerme" después de 15 min de inactividad
- Primera carga puede tardar 30-60 segundos
- Considera Railway o PythonAnywhere para evitar esto

---

## 🎓 Tips para tu Presentación

1. **Despliega con anticipación**
   - Hazlo al menos 2-3 días antes
   - Prueba todo exhaustivamente

2. **Ten un plan B**
   - Guarda capturas de pantalla
   - Ten un video de demostración
   - Considera ejecutar localmente como respaldo

3. **Imprime los QR codes**
   - Usa `create_qr_pdf.py` para generar PDFs
   - Imprime en cartulina o papel grueso
   - Plastifícalos si es posible

4. **Prepara dispositivos**
   - Ten al menos 2 dispositivos para demostrar
   - Carga las baterías completamente
   - Prueba la conexión WiFi del lugar

5. **Documenta todo**
   - Toma fotos del proceso
   - Guarda logs de despliegue
   - Prepara slides con arquitectura técnica

---

## 📞 URLs de Soporte

- **Render Docs:** https://render.com/docs
- **Railway Docs:** https://docs.railway.app
- **PythonAnywhere Help:** https://help.pythonanywhere.com
- **Flask Docs:** https://flask.palletsprojects.com

---

## ✅ Recomendación Final

Para tu proyecto universitario, recomiendo:

1. **Render.com** como servidor principal (gratis, fácil, confiable)
2. Genera los PDFs de QR codes para imprimir
3. Prueba todo en móvil antes de la presentación
4. Ten el proyecto corriendo localmente como respaldo

¡Éxito con tu presentación! 🎉
