// Funciones globales para todos los juegos

// Prevenir zoom en dispositivos móviles
document.addEventListener('gesturestart', function (e) {
    e.preventDefault();
});

// Función para obtener posición del toque/click
function getInputPosition(e, canvas) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    
    let x, y;
    
    if (e.touches && e.touches.length > 0) {
        x = (e.touches[0].clientX - rect.left) * scaleX;
        y = (e.touches[0].clientY - rect.top) * scaleY;
    } else {
        x = (e.clientX - rect.left) * scaleX;
        y = (e.clientY - rect.top) * scaleY;
    }
    
    return { x, y };
}

// Función para generar color aleatorio
function randomColor() {
    const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', 
                   '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B739', '#52B788'];
    return colors[Math.floor(Math.random() * colors.length)];
}

// Función para reproducir sonido de éxito
function playSuccessSound() {
    // Crear un contexto de audio simple
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.value = 800;
    oscillator.type = 'sine';
    
    gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
    
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.5);
}

// Función para mostrar mensaje de felicitación
function showCelebration(message = "¡Muy bien! 🎉") {
    const celebration = document.createElement('div');
    celebration.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.95);
        padding: 30px 50px;
        border-radius: 20px;
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        z-index: 1000;
        animation: celebrationPop 0.5s ease;
    `;
    celebration.textContent = message;
    document.body.appendChild(celebration);
    
    setTimeout(() => {
        celebration.remove();
    }, 2000);
}

// Añadir estilos de animación
const style = document.createElement('style');
style.textContent = `
    @keyframes celebrationPop {
        0% {
            transform: translate(-50%, -50%) scale(0);
            opacity: 0;
        }
        50% {
            transform: translate(-50%, -50%) scale(1.2);
        }
        100% {
            transform: translate(-50%, -50%) scale(1);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);
