// Referencias al DOM
const imageUrlInput = document.getElementById('imageUrl');
const addBtn = document.getElementById('addBtn');
const deleteBtn = document.getElementById('deleteBtn');
const gallery = document.getElementById('gallery');

// 1. Función para agregar imagen
addBtn.addEventListener('click', () => {
    const url = imageUrlInput.value;

    if (url === "") {
        alert("Por favor, ingresa una URL válida.");
        return;
    }

    // Crear elemento img
    const newImg = document.createElement('img');
    newImg.src = url;
    newImg.alt = "Imagen de la galería";

    // Evento para seleccionar la imagen
    newImg.addEventListener('click', function() {
        // Quitar la clase 'selected' de cualquier otra imagen
        const currentSelected = document.querySelector('.selected');
        if (currentSelected) {
            currentSelected.classList.remove('selected');
        }
        // Añadir a la imagen actual
        this.classList.toggle('selected');
    });

    // Agregar a la galería y limpiar input
    gallery.appendChild(newImg);
    imageUrlInput.value = "";
});

// 2. Función para eliminar imagen seleccionada
deleteBtn.addEventListener('click', () => {
    const selectedImg = document.querySelector('.selected');
    if (selectedImg) {
        selectedImg.remove();
    } else {
        alert("Selecciona una imagen primero haciendo clic en ella.");
    }
});

// 3. Atajos de teclado (Keydown)
document.addEventListener('keydown', (event) => {
    if (event.key === "Delete" || event.key === "Backspace") {
        const selectedImg = document.querySelector('.selected');
        if (selectedImg) selectedImg.remove();
    }
});