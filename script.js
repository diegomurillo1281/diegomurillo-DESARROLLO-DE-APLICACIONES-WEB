const imageUrlInput = document.getElementById("imageUrl");
const addBtn = document.getElementById("addBtn");
const deleteBtn = document.getElementById("deleteBtn");
const gallery = document.getElementById("gallery");

let selectedImage = null;

// Agregar imagen
addBtn.addEventListener("click", () => {
    const url = imageUrlInput.value.trim();

    if (url === "") {
        alert("Por favor ingresa una URL válida");
        return;
    }

    const img = document.createElement("img");
    img.src = url;

    img.addEventListener("click", () => {
        if (selectedImage) {
            selectedImage.classList.remove("selected");
        }
        img.classList.add("selected");
        selectedImage = img;
    });

    gallery.appendChild(img);
    imageUrlInput.value = "";
});

// Eliminar imagen seleccionada
deleteBtn.addEventListener("click", () => {
    if (!selectedImage) {
        alert("Selecciona una imagen primero");
        return;
    }

    gallery.removeChild(selectedImage);
    selectedImage = null;
});

