const form = document.getElementById('registrationForm');
const submitBtn = document.getElementById('submitBtn');

// Objeto para rastrear la validez de cada campo
const fieldsStatus = {
    username: false,
    email: false,
    password: false,
    confirmPassword: false,
    age: false
};

// Expresiones Regulares (Regex)
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const passwordRegex = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/;

// Función para mostrar/ocultar errores y cambiar clases
const validateField = (id, isValid, message = "") => {
    const input = document.getElementById(id);
    const errorSpan = document.getElementById(`${id}Error`);
    
    fieldsStatus[id] = isValid;

    if (isValid) {
        input.classList.remove('invalid');
        input.classList.add('valid');
        errorSpan.textContent = "";
    } else {
        input.classList.remove('valid');
        input.classList.add('invalid');
        errorSpan.textContent = message;
    }
    
    checkFormValidity();
};

// Habilitar o deshabilitar botón de envío
const checkFormValidity = () => {
    const allValid = Object.values(fieldsStatus).every(status => status === true);
    submitBtn.disabled = !allValid;
};

// Event Listeners para validación en tiempo real
document.getElementById('username').addEventListener('input', (e) => {
    const value = e.target.value.trim();
    validateField('username', value.length >= 3, "Mínimo 3 caracteres.");
});

document.getElementById('email').addEventListener('input', (e) => {
    validateField('email', emailRegex.test(e.target.value), "Formato de correo inválido.");
});

document.getElementById('password').addEventListener('input', (e) => {
    const value = e.target.value;
    validateField('password', passwordRegex.test(value), "Debe tener 8+ caracteres, un número y un símbolo.");
    // Re-validar confirmación si la contraseña cambia
    const confirmVal = document.getElementById('confirmPassword').value;
    if (confirmVal) {
        validateField('confirmPassword', confirmVal === value, "Las contraseñas no coinciden.");
    }
});

document.getElementById('confirmPassword').addEventListener('input', (e) => {
    const passValue = document.getElementById('password').value;
    validateField('confirmPassword', e.target.value === passValue, "Las contraseñas no coinciden.");
});

document.getElementById('age').addEventListener('input', (e) => {
    const value = parseInt(e.target.value);
    validateField('age', value >= 18, "Debes ser mayor de 18 años.");
});

// Manejo del envío
form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert("¡Formulario enviado con éxito!");
    form.reset();
    // Limpiar clases y estados después del reset
    Object.keys(fieldsStatus).forEach(key => fieldsStatus[key] = false);
    document.querySelectorAll('input').forEach(input => input.classList.remove('valid'));
    submitBtn.disabled = true;
});