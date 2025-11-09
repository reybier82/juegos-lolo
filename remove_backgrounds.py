#!/usr/bin/env python3
"""
Script para eliminar fondos blancos de las imágenes
"""
from PIL import Image
import os

def remove_white_background(input_path, output_path):
    """Elimina el fondo blanco de una imagen y la guarda con transparencia"""
    # Abrir la imagen
    img = Image.open(input_path)
    
    # Convertir a RGBA si no lo está
    img = img.convert("RGBA")
    
    # Obtener datos de píxeles
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Cambiar todos los píxeles blancos y grises claros a transparentes
        # Umbral más bajo para eliminar más agresivamente
        # También verificar que los 3 canales RGB sean similares (gris/blanco)
        r, g, b, a = item
        
        # Si es blanco, gris claro, o muy transparente
        if (r > 220 and g > 220 and b > 220) or a < 50:
            newData.append((255, 255, 255, 0))  # Completamente transparente
        # Si es gris medio claro (diferencia entre canales < 30)
        elif r > 200 and g > 200 and b > 200 and abs(r-g) < 30 and abs(g-b) < 30 and abs(r-b) < 30:
            newData.append((255, 255, 255, 0))  # Transparente
        else:
            newData.append(item)
    
    img.putdata(newData)
    
    # Guardar como PNG con transparencia
    img.save(output_path, "PNG")
    print(f"✓ Procesado: {output_path}")

# Procesar las imágenes
images_to_process = [
    ('assets/img/jirafa.png', 'assets/img/jirafa.png'),
    ('assets/img/jamon.png', 'assets/img/jamon.png'),
    ('assets/img/jugo.png', 'assets/img/jugo.png'),
]

print("Eliminando fondos blancos...")
for input_file, output_file in images_to_process:
    if os.path.exists(input_file):
        remove_white_background(input_file, output_file)
    else:
        print(f"✗ No encontrado: {input_file}")

print("\n¡Proceso completado!")
