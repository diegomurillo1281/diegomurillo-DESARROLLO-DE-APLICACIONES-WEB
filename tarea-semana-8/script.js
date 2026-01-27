// 1. Botón de Alerta Personalizada
function mostrarAlerta() {
    alert("🚀 ¡Felicidades! Has desbloqueado un cupón del 20%: BOOTSTRAP2026");
}

// 2. Validación Dinámica del Formulario
const form = document.getElementById('contactForm');
const mensajeExito = document.getElementById('mensajeExito');

form.addEventListener('submit', function (event) {
    // Si el formulario no es válido según los atributos de HTML5
    if (!form.checkValidity()) {
        event.preventDefault(); // Detiene el envío
        event.stopPropagation(); // Detiene la propagación
    } else {
        event.preventDefault(); // Detiene el envío real para mostrar el éxito
        mensajeExito.classList.remove('d-none'); // Muestra mensaje de éxito
        form.reset(); // Limpia los campos
        form.classList.remove('was-validated'); // Limpia los estados de validación
        return;
    }

    // Añade la clase de Bootstrap para mostrar errores visuales
    form.classList.add('was-validated');
}, false);