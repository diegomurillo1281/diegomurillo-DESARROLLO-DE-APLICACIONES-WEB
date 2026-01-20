// 1. Arreglo inicial de productos
const productos = [
    { nombre: "Laptop Pro", precio: 1200, descripcion: "Potente para diseño y programación." },
    { nombre: "Mouse Inalámbrico", precio: 25, descripcion: "Económico y ergonómico." },
    { nombre: "Teclado Mecánico", precio: 80, descripcion: "Luces RGB y switches azules." }
];

// 2. Referencias a elementos del DOM
const listaUL = document.getElementById('lista-productos');
const botonAgregar = document.getElementById('btn-agregar');

// 3. Función para renderizar un producto usando plantillas (Template Literals)
function renderizarProductos() {
    // Limpiamos la lista para evitar duplicados al renderizar de nuevo
    listaUL.innerHTML = "";

    productos.forEach(producto => {
        const li = document.createElement('li');
        li.className = "producto";
        
        // Plantilla dinámica
        li.innerHTML = `
            <strong>${producto.nombre}</strong><br>
            <span class="precio">Precio: $${producto.precio}</span><br>
            <small>${producto.descripcion}</small>
        `;
        
        listaUL.appendChild(li);
    });
}

// 4. Función para agregar un nuevo producto
function agregarProducto() {
    const nuevo = {
        nombre: "Nuevo Producto " + (productos.length + 1),
        precio: Math.floor(Math.random() * 100) + 10,
        descripcion: "Descripción generada automáticamente."
    };

    productos.push(nuevo);
    renderizarProductos(); // Volvemos a dibujar la lista
}

// 5. Inicialización
// Ejecutar al cargar la página
document.addEventListener('DOMContentLoaded', renderizarProductos);

// Escuchar el click del botón
botonAgregar.addEventListener('click', agregarProducto);