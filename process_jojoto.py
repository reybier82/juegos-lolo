#!/usr/bin/env python3
"""
Script para procesar la imagen del jojoto (convertir AVIF a PNG y eliminar fondo)
"""
from PIL import Image
import pillow_avif  # Importar el plugin AVIF
import os

def remove_white_background(input_path, output_path):
    """Elimina el fondo blanco de una imagen y la guarda con transparencia"""
    print(f"Procesando: {input_path}")
    
    # Abrir la imagen
    img = Image.open(input_path)
    
    # Convertir a RGBA si no lo está
    img = img.convert("RGBA")
    
    # Obtener datos de píxeles
    datas = img.getdata()
    
    newData = []
    for item in datas:
        r, g, b, a = item
        
        # Si es blanco, gris claro, o muy transparente
        if (r > 220 and g > 220 and b > 220) or a < 50:
            newData.append((255, 255, 255, 0))  # Completamente transparente
        # Si es gris medio claro
        elif r > 200 and g > 200 and b > 200 and abs(r-g) < 30 and abs(g-b) < 30 and abs(r-b) < 30:
            newData.append((255, 255, 255, 0))  # Transparente
        else:
            newData.append(item)
    
    img.putdata(newData)
    
    # Guardar como PNG con transparencia
    img.save(output_path, "PNG")
    print(f"✓ Guardado como PNG: {output_path}")

# Procesar jojoto
input_file = 'assets/img/jojoto.avif'
output_file = 'assets/img/jojoto.png'

if os.path.exists(input_file):
    print("Procesando jojoto.avif...")
    remove_white_background(input_file, output_file)
    print(f"\n✓ Jojoto procesado y convertido a PNG")
    print(f"  Ahora usa: jojoto.png en lugar de jojoto.avif")
else:
    print(f"✗ No se encontró: {input_file}")
