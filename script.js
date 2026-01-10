const gallery = document.getElementById("gallery");
const imageUrlInput = document.getElementById("imageUrl");
const addBtn = document.getElementById("addBtn");
const deleteBtn = document.getElementById("deleteBtn");

let selectedImage = null;

// 🔹 IMÁGENES LOCALES PRECARGADAS
const imagenesIniciales = [
    "assets/img/cerro_santa_ana.jpg",
    "assets/img/malecon2000.jpg",
    "assets/img/parque_historico.jpg"
];

// 🔹 FUNCIÓN PARA CREAR IMÁGENES
function crearImagen(src) {
    const img = document.createElement("img");
    img.src = src;

    img.addEventListener("click", () => {
        if (selectedImage) {
            selectedImage.classList.remove("selected");
        }
        selectedImage = img;
        img.classList.add("selected");
    });

    gallery.appendChild(img);
}

// 🔹 CARGAR IMÁGENES LOCALES AL INICIO
imagenesIniciales.forEach(src => crearImagen(src));

// 🔹 AGREGAR IMAGEN DESDE URL
addBtn.addEventListener("click", () => {
    const url = imageUrlInput.value.trim();

    if (url === "") {
        alert("Por favor ingresa una URL válida");
        return;
    }

    crearImagen(url);
    imageUrlInput.value = "";
});

// 🔹 ELIMINAR IMAGEN SELECCIONADA
deleteBtn.addEventListener("click", () => {
    if (!selectedImage) {
        alert("Selecciona una imagen primero");
        return;
    }

    gallery.removeChild(selectedImage);
    selectedImage = null;
});
