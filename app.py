from flask import Flask, render_template, send_file, send_from_directory
import os

app = Flask(__name__)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    """Servir archivos de la carpeta assets"""
    return send_from_directory('assets', filename)

# Lista de letras del abecedario
LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Descripción de cada juego
JUEGOS = {
    'A': {'nombre': 'Aplastar Burbujas', 'descripcion': 'Toca las burbujas con la letra A'},
    'B': {'nombre': 'Buscar Objetos', 'descripcion': 'Encuentra objetos que empiezan con B'},
    'C': {'nombre': 'Colorear', 'descripcion': 'Colorea la letra C'},
    'D': {'nombre': 'Dibujar', 'descripcion': 'Dibuja sobre la letra D'},
    'E': {'nombre': 'La Ducha del Elefante', 'descripcion': 'Arrastra la nube E para darle una ducha al elefante'},
    'F': {'nombre': 'Flores Mágicas', 'descripcion': 'Haz crecer flores tocándolas'},
    'G': {'nombre': 'El Ovillo del Gato', 'descripcion': 'Traza el camino para que el gato llegue al ovillo'},
    'H': {'nombre': 'Hacer Música', 'descripcion': 'Toca instrumentos musicales'},
    'I': {'nombre': 'Iluminar Estrellas', 'descripcion': 'Ilumina estrellas con la letra I'},
    'J': {'nombre': 'Jabón y Burbujas', 'descripcion': 'Juega con burbujas de jabón'},
    'K': {'nombre': 'Karaoke', 'descripcion': 'Escucha el sonido de la K'},
    'L': {'nombre': 'Laberinto', 'descripcion': 'Sigue el camino de la letra L'},
    'M': {'nombre': 'Mover Animales', 'descripcion': 'Mueve animales que empiezan con M'},
    'N': {'nombre': 'Números', 'descripcion': 'Cuenta con la letra N'},
    'O': {'nombre': 'Ordenar Círculos', 'descripcion': 'Ordena círculos con la letra O'},
    'P': {'nombre': 'Pintar', 'descripcion': 'Pinta la letra P con tus dedos'},
    'Q': {'nombre': 'Queso para Ratón', 'descripcion': 'Arrastra el queso al ratón'},
    'R': {'nombre': 'Rompecabezas', 'descripcion': 'Arma el rompecabezas de la R'},
    'S': {'nombre': 'Sonidos', 'descripcion': 'Escucha sonidos de animales con S'},
    'T': {'nombre': 'Tambor', 'descripcion': 'Toca el tambor y haz ritmos'},
    'U': {'nombre': 'Uvas para Contar', 'descripcion': 'Cuenta las uvas'},
    'V': {'nombre': 'Volar Mariposas', 'descripcion': 'Haz volar mariposas'},
    'W': {'nombre': 'Waffles', 'descripcion': 'Decora waffles deliciosos'},
    'X': {'nombre': 'Xilófono', 'descripcion': 'Toca el xilófono musical'},
    'Y': {'nombre': 'Yo-yo', 'descripcion': 'Juega con el yo-yo'},
    'Z': {'nombre': 'Zoológico', 'descripcion': 'Descubre animales del zoológico'}
}

@app.route('/')
def index():
    """Página principal con el menú del abecedario"""
    return render_template('index.html', letras=LETRAS, juegos=JUEGOS)

@app.route('/juego/<letra>')
def juego(letra):
    """Página de juego para cada letra"""
    letra = letra.upper()
    if letra not in LETRAS:
        return "Letra no encontrada", 404
    
    return render_template(f'juegos/{letra}.html', 
                         letra=letra, 
                         juego=JUEGOS.get(letra, {}))

@app.route('/qr/<letra>')
def mostrar_qr(letra):
    """Muestra el código QR de una letra"""
    letra = letra.upper()
    qr_path = f'static/qr/qr_{letra}.png'
    if os.path.exists(qr_path):
        return send_file(qr_path, mimetype='image/png')
    return "QR no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
