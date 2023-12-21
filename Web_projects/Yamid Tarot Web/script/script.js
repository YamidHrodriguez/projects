const nav = document.getElementById('nav');
const abrir = document.getElementById('abrir');
const cerrar = document.getElementById('cerrar');
const header = document.getElementById('header');

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
    header.classList.add("visible")
});

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
    header.classList.remove("visible")
}); 