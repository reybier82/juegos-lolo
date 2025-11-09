"""
Script para generar las plantillas HTML de los juegos restantes del abecedario
"""

import os

# Configuración de juegos restantes
games_config = {
    'G': {
        'title': 'Girar',
        'emoji': '🔄',
        'description': '¡Gira objetos con forma de G!',
        'game_type': 'spin'
    },
    'H': {
        'title': 'Hacer Música',
        'emoji': '🎵',
        'description': '¡Toca instrumentos musicales!',
        'game_type': 'music'
    },
    'I': {
        'title': 'Iluminar Estrellas',
        'emoji': '⭐',
        'description': '¡Ilumina estrellas con la letra I!',
        'game_type': 'stars'
    },
    'J': {
        'title': 'Jabón y Burbujas',
        'emoji': '🫧',
        'description': '¡Juega con burbujas de jabón!',
        'game_type': 'bubbles'
    },
    'K': {
        'title': 'Karaoke',
        'emoji': '🎤',
        'description': '¡Escucha el sonido de la K!',
        'game_type': 'sound'
    },
    'L': {
        'title': 'Laberinto',
        'emoji': '🌀',
        'description': '¡Sigue el camino de la letra L!',
        'game_type': 'maze'
    },
    'M': {
        'title': 'Mover Animales',
        'emoji': '🐵',
        'description': '¡Mueve animales que empiezan con M!',
        'game_type': 'drag'
    },
    'N': {
        'title': 'Números',
        'emoji': '🔢',
        'description': '¡Cuenta con la letra N!',
        'game_type': 'count'
    },
    'O': {
        'title': 'Ordenar Círculos',
        'emoji': '⭕',
        'description': '¡Ordena círculos con la letra O!',
        'game_type': 'sort'
    },
    'P': {
        'title': 'Pintar',
        'emoji': '🎨',
        'description': '¡Pinta la letra P con tus dedos!',
        'game_type': 'paint'
    },
    'Q': {
        'title': 'Queso para Ratón',
        'emoji': '🧀',
        'description': '¡Arrastra el queso al ratón!',
        'game_type': 'drag_drop'
    },
    'R': {
        'title': 'Rompecabezas',
        'emoji': '🧩',
        'description': '¡Arma el rompecabezas de la R!',
        'game_type': 'puzzle'
    },
    'S': {
        'title': 'Sonidos',
        'emoji': '🐍',
        'description': '¡Escucha sonidos de animales con S!',
        'game_type': 'sound_animals'
    },
    'T': {
        'title': 'Tambor',
        'emoji': '🥁',
        'description': '¡Toca el tambor y haz ritmos!',
        'game_type': 'drum'
    },
    'U': {
        'title': 'Uvas para Contar',
        'emoji': '🍇',
        'description': '¡Cuenta las uvas!',
        'game_type': 'count_grapes'
    },
    'V': {
        'title': 'Volar Mariposas',
        'emoji': '🦋',
        'description': '¡Haz volar mariposas!',
        'game_type': 'butterflies'
    },
    'W': {
        'title': 'Waffles',
        'emoji': '🧇',
        'description': '¡Decora waffles deliciosos!',
        'game_type': 'decorate'
    },
    'X': {
        'title': 'Xilófono',
        'emoji': '🎹',
        'description': '¡Toca el xilófono musical!',
        'game_type': 'xylophone'
    },
    'Y': {
        'title': 'Yo-yo',
        'emoji': '🪀',
        'description': '¡Juega con el yo-yo!',
        'game_type': 'yoyo'
    },
    'Z': {
        'title': 'Zoológico',
        'emoji': '🦁',
        'description': '¡Descubre animales del zoológico!',
        'game_type': 'zoo'
    }
}

def generate_game_html(letter, config):
    """Genera el HTML para un juego específico"""
    
    # Plantilla base para juegos simples de tocar/click
    template = f'''{{%extends "base.html" %}}

{{% block title %}}Letra {letter} - {config['title']}{{% endblock %}}

{{% block content %}}
<div class="game-header">
    <h1 class="game-title">{config['emoji']} Letra {letter} - {config['title']}</h1>
    <p class="game-description">{config['description']}</p>
    <a href="{{{{ url_for('index') }}}}" class="back-button">🏠 Volver al Menú</a>
</div>

<div class="game-canvas-container">
    <canvas id="gameCanvas" width="800" height="600"></canvas>
</div>
{{% endblock %}}

{{% block extra_js %}}
<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

function resizeCanvas() {{
    const container = canvas.parentElement;
    const maxWidth = Math.min(800, container.clientWidth - 40);
    const scale = maxWidth / 800;
    canvas.style.width = maxWidth + 'px';
    canvas.style.height = (600 * scale) + 'px';
}}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

let score = 0;
let items = [];

// Clase de item interactivo
class Item {{
    constructor() {{
        this.x = Math.random() * (canvas.width - 100) + 50;
        this.y = Math.random() * (canvas.height - 150) + 100;
        this.size = 60 + Math.random() * 40;
        this.color = randomColor();
        this.clicked = false;
        this.wobble = Math.random() * Math.PI * 2;
    }}
    
    update() {{
        this.wobble += 0.05;
    }}
    
    draw() {{
        if (this.clicked) {{
            ctx.globalAlpha = 0.3;
        }}
        
        const offsetY = Math.sin(this.wobble) * 5;
        
        // Dibujar emoji o forma
        ctx.font = `${{this.size}}px Arial`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('{config['emoji']}', this.x, this.y + offsetY);
        
        // Letra {letter}
        ctx.font = `bold ${{this.size * 0.4}}px Arial`;
        ctx.fillStyle = this.color;
        ctx.strokeStyle = 'white';
        ctx.lineWidth = 3;
        ctx.strokeText('{letter}', this.x, this.y + offsetY);
        ctx.fillText('{letter}', this.x, this.y + offsetY);
        
        ctx.globalAlpha = 1;
    }}
    
    isClicked(x, y) {{
        const dist = Math.sqrt((x - this.x) ** 2 + (y - this.y) ** 2);
        return dist < this.size / 2;
    }}
    
    click() {{
        if (!this.clicked) {{
            this.clicked = true;
            score++;
            playSuccessSound();
            
            if (score % 5 === 0) {{
                showCelebration('¡Muy bien! 🎉');
            }}
        }}
    }}
}}

// Crear items iniciales
for (let i = 0; i < 6; i++) {{
    items.push(new Item());
}}

// Manejo de input
function handleInput(e) {{
    e.preventDefault();
    const pos = getInputPosition(e, canvas);
    
    items.forEach(item => {{
        if (item.isClicked(pos.x, pos.y)) {{
            item.click();
        }}
    }});
    
    // Regenerar items si todos fueron clickeados
    const allClicked = items.every(item => item.clicked);
    if (allClicked) {{
        setTimeout(() => {{
            items = [];
            for (let i = 0; i < 6; i++) {{
                items.push(new Item());
            }}
        }}, 1000);
    }}
}}

canvas.addEventListener('mousedown', handleInput);
canvas.addEventListener('touchstart', handleInput);

// Loop del juego
function gameLoop() {{
    // Fondo
    const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
    gradient.addColorStop(0, '#E8EAF6');
    gradient.addColorStop(1, '#C5CAE9');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Título
    ctx.font = 'bold 35px Arial';
    ctx.fillStyle = '#667eea';
    ctx.textAlign = 'center';
    ctx.fillText('¡Toca los {config['emoji']} con {letter}!', canvas.width / 2, 40);
    
    // Actualizar y dibujar items
    items.forEach(item => {{
        item.update();
        item.draw();
    }});
    
    // Puntuación
    ctx.font = 'bold 40px Arial';
    ctx.fillStyle = '#4CAF50';
    ctx.textAlign = 'left';
    ctx.fillText(`⭐ ${{score}}`, 20, canvas.height - 20);
    
    requestAnimationFrame(gameLoop);
}}

gameLoop();
</script>
{{% endblock %}}
'''
    
    return template

def main():
    """Genera todos los archivos HTML de juegos"""
    templates_dir = 'templates/juegos'
    os.makedirs(templates_dir, exist_ok=True)
    
    for letter, config in games_config.items():
        filename = f'{templates_dir}/{letter}.html'
        
        # Solo crear si no existe
        if not os.path.exists(filename):
            html_content = generate_game_html(letter, config)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f'✓ Creado: {filename}')
        else:
            print(f'⊘ Ya existe: {filename}')
    
    print('\n¡Todos los juegos han sido generados!')

if __name__ == '__main__':
    main()
