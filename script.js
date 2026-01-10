// Referencias a los elementos del DOM
const imageUrlInput = document.getElementById('imageUrl');
const addBtn = document.getElementById('addBtn');
const deleteBtn = document.getElementById('deleteBtn');
const gallery = document.getElementById('gallery');

/**
 * Función para agregar una imagen a la galería
 */
addBtn.addEventListener('click', () => {
    const url = imageUrlInput.value.trim();

    if (url === "") {
        alert("Por favor, ingresa una URL de imagen válida.");
        return;
    }

    // Crear el elemento de imagen
    const newImg = document.createElement('img');
    newImg.src = url;
    newImg.alt = "Imagen de galería";

    // Evento para seleccionar la imagen
    newImg.addEventListener('click', function() {
        // Buscar si ya hay una imagen seleccionada y quitarle la clase
        const currentSelected = document.querySelector('.selected');
        
        if (currentSelected && currentSelected !== this) {
            currentSelected.classList.remove('selected');
        }

        // Alternar selección en la imagen actual
        this.classList.toggle('selected');
    });

    // Añadir la imagen al contenedor y limpiar el input
    gallery.appendChild(newImg);
    imageUrlInput.value = "";
});

/**
 * Función para eliminar la imagen seleccionada
 */
const eliminarImagen = () => {
    const selectedImg = document.querySelector('.selected');
    if (selectedImg) {
        selectedImg.remove();
    } else {
        alert("Por favor, selecciona una imagen primero haciendo clic en ella.");
    }
};

// Evento para el botón de eliminar
deleteBtn.addEventListener('click', eliminarImagen);

// Manejo de eventos de teclado (Atajos)
document.addEventListener('keydown', (event) => {
    // Si se presiona la tecla "Delete" (Suprimir) o "Backspace" (Retroceso)
    if (event.key === "Delete" || event.key === "Backspace") {
        eliminarImagen();
    }
});