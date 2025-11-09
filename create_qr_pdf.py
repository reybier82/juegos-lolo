"""
Script para crear un PDF con todos los códigos QR del abecedario
Útil para imprimir y usar en la presentación
"""

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    from PIL import Image
    import os
except ImportError:
    print("❌ Error: Necesitas instalar reportlab y Pillow")
    print("Ejecuta: pip install reportlab Pillow")
    exit(1)

def create_qr_pdf():
    """Crea un PDF con todos los códigos QR en formato de tarjetas"""
    
    # Verificar que existan los QR codes
    qr_dir = 'static/qr'
    if not os.path.exists(qr_dir):
        print("❌ Error: No se encontró la carpeta de códigos QR")
        print("Ejecuta primero: python3 generate_qr.py")
        return
    
    # Crear PDF
    pdf_filename = 'codigos_qr_abecedario.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4
    
    # Letras del abecedario
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Configuración de layout (3 columnas x 3 filas por página)
    cols = 3
    rows = 3
    items_per_page = cols * rows
    
    margin = 40
    card_width = (width - 2 * margin) / cols
    card_height = (height - 2 * margin) / rows
    
    for i, letra in enumerate(letras):
        # Nueva página cada 9 letras
        if i > 0 and i % items_per_page == 0:
            c.showPage()
        
        # Calcular posición
        page_index = i % items_per_page
        col = page_index % cols
        row = page_index // cols
        
        x = margin + col * card_width
        y = height - margin - (row + 1) * card_height
        
        # Dibujar borde de tarjeta
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.setLineWidth(1)
        c.rect(x + 5, y + 5, card_width - 10, card_height - 10)
        
        # Título de la letra
        c.setFont("Helvetica-Bold", 36)
        c.setFillColorRGB(0.4, 0.49, 0.92)  # Color #667eea
        c.drawCentredString(x + card_width / 2, y + card_height - 40, f"Letra {letra}")
        
        # Código QR
        qr_path = f'{qr_dir}/qr_{letra}.png'
        if os.path.exists(qr_path):
            qr_size = min(card_width, card_height) - 80
            qr_x = x + (card_width - qr_size) / 2
            qr_y = y + 20
            
            try:
                c.drawImage(qr_path, qr_x, qr_y, qr_size, qr_size)
            except Exception as e:
                print(f"⚠️  Error al cargar QR de {letra}: {e}")
        else:
            c.setFont("Helvetica", 10)
            c.setFillColorRGB(1, 0, 0)
            c.drawCentredString(x + card_width / 2, y + card_height / 2, "QR no encontrado")
    
    # Guardar PDF
    c.save()
    print(f"✅ PDF creado exitosamente: {pdf_filename}")
    print(f"📄 Contiene {len(letras)} códigos QR del abecedario")
    print(f"🖨️  Listo para imprimir!")

def create_individual_cards():
    """Crea un PDF con tarjetas individuales (una letra por página)"""
    
    qr_dir = 'static/qr'
    if not os.path.exists(qr_dir):
        print("❌ Error: No se encontró la carpeta de códigos QR")
        return
    
    pdf_filename = 'tarjetas_individuales_qr.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4
    
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    juegos = {
        'A': 'Aplastar Burbujas', 'B': 'Buscar Objetos', 'C': 'Colorear',
        'D': 'Dibujar', 'E': 'Explotar Globos', 'F': 'Flores Mágicas',
        'G': 'Girar', 'H': 'Hacer Música', 'I': 'Iluminar Estrellas',
        'J': 'Jabón y Burbujas', 'K': 'Karaoke', 'L': 'Laberinto',
        'M': 'Mover Animales', 'N': 'Números',
        'O': 'Ordenar Círculos', 'P': 'Pintar', 'Q': 'Queso para Ratón',
        'R': 'Rompecabezas', 'S': 'Sonidos', 'T': 'Tambor',
        'U': 'Uvas para Contar', 'V': 'Volar Mariposas', 'W': 'Waffles',
        'X': 'Xilófono', 'Y': 'Yo-yo', 'Z': 'Zoológico'
    }
    
    for i, letra in enumerate(letras):
        if i > 0:
            c.showPage()
        
        # Fondo de color suave
        c.setFillColorRGB(0.95, 0.95, 1)
        c.rect(0, 0, width, height, fill=1, stroke=0)
        
        # Título grande
        c.setFont("Helvetica-Bold", 72)
        c.setFillColorRGB(0.4, 0.49, 0.92)
        c.drawCentredString(width / 2, height - 100, letra)
        
        # Nombre del juego
        c.setFont("Helvetica-Bold", 24)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        c.drawCentredString(width / 2, height - 150, juegos.get(letra, ''))
        
        # Código QR centrado
        qr_path = f'{qr_dir}/qr_{letra}.png'
        if os.path.exists(qr_path):
            qr_size = 300
            qr_x = (width - qr_size) / 2
            qr_y = (height - qr_size) / 2 - 50
            
            # Borde blanco alrededor del QR
            c.setFillColorRGB(1, 1, 1)
            c.rect(qr_x - 20, qr_y - 20, qr_size + 40, qr_size + 40, fill=1, stroke=0)
            
            c.drawImage(qr_path, qr_x, qr_y, qr_size, qr_size)
        
        # Instrucciones
        c.setFont("Helvetica", 16)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        c.drawCentredString(width / 2, 100, "Escanea el código QR con tu celular")
        c.drawCentredString(width / 2, 70, "para jugar")
    
    c.save()
    print(f"✅ Tarjetas individuales creadas: {pdf_filename}")
    print(f"📄 Una letra por página - perfecto para carteles grandes")

if __name__ == '__main__':
    print("🎨 Generando PDFs con códigos QR...\n")
    
    print("1️⃣  Creando PDF con múltiples QR por página...")
    create_qr_pdf()
    
    print("\n2️⃣  Creando tarjetas individuales...")
    create_individual_cards()
    
    print("\n✨ ¡Listo! Tienes dos PDFs:")
    print("   - codigos_qr_abecedario.pdf (9 por página)")
    print("   - tarjetas_individuales_qr.pdf (1 por página)")
