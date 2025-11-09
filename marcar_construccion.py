#!/usr/bin/env python3
"""
Script para marcar juegos como "En Construcción"
"""

import os

# Juegos que están listos (NO modificar)
JUEGOS_LISTOS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Q']

# Todas las letras
TODAS_LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Información de cada juego
JUEGOS_INFO = {
    'E': {'nombre': 'La Ducha del Elefante', 'emoji': '🐘'},
    'G': {'nombre': 'El Ovillo del Gato', 'emoji': '🐱'},
    'H': {'nombre': 'Hacer Música', 'emoji': '🎵'},
    'I': {'nombre': 'Iluminar Estrellas', 'emoji': '⭐'},
    'J': {'nombre': 'Jabón y Burbujas', 'emoji': '🫧'},
    'K': {'nombre': 'Karaoke', 'emoji': '🎤'},
    'L': {'nombre': 'Laberinto', 'emoji': '🌀'},
    'M': {'nombre': 'Mover Animales', 'emoji': '🐵'},
    'N': {'nombre': 'Números', 'emoji': '🔢'},
    'O': {'nombre': 'Ordenar Círculos', 'emoji': '⭕'},
    'P': {'nombre': 'Pintar', 'emoji': '🎨'},
    'R': {'nombre': 'Rompecabezas', 'emoji': '🧩'},
    'S': {'nombre': 'Sonidos', 'emoji': '🐍'},
    'T': {'nombre': 'Tambor', 'emoji': '🥁'},
    'U': {'nombre': 'Uvas para Contar', 'emoji': '🍇'},
    'V': {'nombre': 'Volar Mariposas', 'emoji': '🦋'},
    'W': {'nombre': 'Waffles', 'emoji': '🧇'},
    'X': {'nombre': 'Xilófono', 'emoji': '🎹'},
    'Y': {'nombre': 'Yo-yo', 'emoji': '🪀'},
    'Z': {'nombre': 'Zoológico', 'emoji': '🦁'}
}

PLANTILLA_CONSTRUCCION = """{{% extends "base.html" %}}

{{% block title %}}Letra {letra} - {nombre}{{% endblock %}}

{{% block content %}}
<div class="game-header">
    <h1 class="game-title">{emoji} Letra {letra} - {nombre}</h1>
    <p class="game-description">¡Próximamente disponible!</p>
    <a href="{{{{ url_for('index') }}}}" class="back-button">🏠 Volver al Menú</a>
</div>

<div class="game-canvas-container">
    <div style="text-align: center; padding: 100px 20px;">
        <h2 style="font-size: 5rem; margin-bottom: 20px;">🚧</h2>
        <h2 style="font-size: 2.5rem; color: #667eea; margin-bottom: 20px;">En Construcción</h2>
        <p style="font-size: 1.5rem; color: #666;">Este juego estará disponible próximamente</p>
    </div>
</div>
{{% endblock %}}
"""

def marcar_juegos_construccion():
    """Marca los juegos no listos como 'En Construcción'"""
    
    templates_dir = 'templates/juegos'
    
    for letra in TODAS_LETRAS:
        if letra in JUEGOS_LISTOS:
            print(f"✅ {letra} - Ya está listo, no se modifica")
            continue
        
        # Obtener info del juego
        info = JUEGOS_INFO.get(letra, {'nombre': 'Juego', 'emoji': '🎮'})
        
        # Crear contenido
        contenido = PLANTILLA_CONSTRUCCION.format(
            letra=letra,
            nombre=info['nombre'],
            emoji=info['emoji']
        )
        
        # Escribir archivo
        archivo = os.path.join(templates_dir, f'{letra}.html')
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        
        print(f"🚧 {letra} - Marcado como 'En Construcción'")

if __name__ == '__main__':
    print("🔨 Marcando juegos como 'En Construcción'...\n")
    marcar_juegos_construccion()
    print("\n✅ ¡Proceso completado!")
    print(f"\nJuegos listos: {', '.join(JUEGOS_LISTOS)}")
    print(f"Juegos en construcción: {len(TODAS_LETRAS) - len(JUEGOS_LISTOS)}")
