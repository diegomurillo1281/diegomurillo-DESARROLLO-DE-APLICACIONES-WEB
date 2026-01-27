// Función para el botón de alerta personalizada
function mostrarAlerta() {
    alert("¡Hola! Esta es una alerta personalizada desde JavaScript 🚀");
}

// Validación del Formulario
const form = document.getElementById('contactForm');
const errorMsg = document.getElementById('errorMsg');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que la página se recargue
    
    const nombre = document.getElementById('nombre').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensaje = document.getElementById('mensaje').value.trim();

    if (nombre === "" || email === "" || mensaje === "") {
        errorMsg.textContent = "Por favor, completa todos los campos obligatorios.";
    } else {
        errorMsg.classList.remove('text-danger');
        errorMsg.classList.add('text-success');
        errorMsg.textContent = "¡Formulario enviado con éxito!";
        form.reset(); // Limpia los campos
    }
});