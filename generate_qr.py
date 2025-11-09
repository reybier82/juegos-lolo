import qrcode
import os

# URL base - CAMBIAR ESTO cuando tengas el servidor desplegado
BASE_URL = "http://localhost:5000"

# Crear directorio para QR codes si no existe
os.makedirs('static/qr', exist_ok=True)

# Lista de letras del abecedario
LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def generar_qr_codes():
    """Genera códigos QR para cada letra del abecedario"""
    for letra in LETRAS:
        # URL del juego
        url = f"{BASE_URL}/juego/{letra}"
        
        # Crear código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Crear imagen
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Guardar imagen
        filename = f'static/qr/qr_{letra}.png'
        img.save(filename)
        print(f"✓ Código QR generado para la letra {letra}: {filename}")

if __name__ == '__main__':
    print("Generando códigos QR para el abecedario...")
    generar_qr_codes()
    print("\n¡Todos los códigos QR han sido generados!")
    print(f"Ubicación: static/qr/")
    print(f"\nNOTA: Recuerda actualizar BASE_URL en generate_qr.py cuando despliegues el servidor")
