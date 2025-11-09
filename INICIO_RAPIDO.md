# 🚀 Inicio Rápido - 5 Minutos

## Opción 1: Ejecutar Localmente (Recomendado para Probar)

### Paso 1: Instalar dependencias
```bash
cd "/home/hazling/Escritorio/Juegos Lorena"
pip3 install Flask qrcode Pillow gunicorn
```

### Paso 2: Generar códigos QR
```bash
python3 generate_qr.py
```

### Paso 3: Ejecutar la aplicación
```bash
python3 app.py
```

### Paso 4: Abrir en el navegador
```
http://localhost:5000
```

**¡Listo! Ya puedes probar todos los juegos.**

---

## Opción 2: Probar en tu Celular (Misma Red WiFi)

### Paso 1: Encuentra tu IP local
```bash
hostname -I
```
Ejemplo de salida: `192.168.1.100`

### Paso 2: Ejecuta la app (si no está corriendo)
```bash
python3 app.py
```

### Paso 3: En tu celular, abre el navegador y ve a:
```
http://192.168.1.100:5000
```
(Reemplaza con tu IP real)

---

## Opción 3: Desplegar en Internet (Render.com)

### Requisitos previos:
- Cuenta de GitHub
- Cuenta de Render.com (gratis)

### Pasos:

1. **Sube el código a GitHub:**
```bash
cd "/home/hazling/Escritorio/Juegos Lorena"
git init
git add .
git commit -m "Juegos educativos del abecedario"

# Crea un repo en github.com y luego:
git remote add origin https://github.com/TU_USUARIO/juegos-abecedario.git
git push -u origin main
```

2. **En Render.com:**
   - New + → Web Service
   - Conecta tu repo de GitHub
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Click "Create Web Service"

3. **Espera 2-3 minutos** y tendrás tu URL pública:
   ```
   https://tu-app.onrender.com
   ```

4. **Actualiza los QR codes:**
   - Edita `generate_qr.py` línea 6:
     ```python
     BASE_URL = "https://tu-app.onrender.com"
     ```
   - Regenera:
     ```bash
     python3 generate_qr.py
     git add static/qr/
     git commit -m "Update QR codes"
     git push
     ```

---

## 🎨 Imprimir Códigos QR

### Generar PDF con todos los QR:
```bash
pip3 install reportlab
python3 create_qr_pdf.py
```

Esto creará dos PDFs:
- `codigos_qr_abecedario.pdf` (9 por página)
- `tarjetas_individuales_qr.pdf` (1 por página)

---

## ❓ Problemas Comunes

### "pip3: command not found"
```bash
sudo apt install python3-pip
```

### "Port 5000 already in use"
```bash
sudo lsof -t -i:5000 | xargs kill -9
```

### Los juegos no cargan
- Verifica que estés en la carpeta correcta
- Asegúrate de que `static/` y `templates/` existen
- Revisa la consola del navegador (F12)

---

## 📱 Para tu Presentación

### Antes de presentar:

1. ✅ Prueba todos los juegos en móvil
2. ✅ Imprime los códigos QR
3. ✅ Ten el proyecto corriendo localmente como respaldo
4. ✅ Prepara 2-3 dispositivos para demostrar
5. ✅ Carga las baterías completamente

### Durante la presentación:

- Muestra la página principal proyectada
- Deja que los profesores escaneen los QR codes
- Demuestra 3-4 juegos diferentes
- Explica la arquitectura técnica
- Menciona la optimización móvil

---

## 📚 Documentación Completa

- **README.md** - Visión general del proyecto
- **INSTRUCCIONES.md** - Guía detallada de instalación
- **DESPLIEGUE.md** - Guía completa de despliegue
- **RESUMEN_PROYECTO.md** - Resumen ejecutivo

---

## 🎯 Siguiente Paso

**Ejecuta ahora mismo:**
```bash
cd "/home/hazling/Escritorio/Juegos Lorena"
pip3 install Flask qrcode Pillow
python3 generate_qr.py
python3 app.py
```

**Luego abre:** http://localhost:5000

¡Disfruta tus juegos educativos! 🎉
