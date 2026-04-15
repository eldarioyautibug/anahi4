
  function navegar(seccionMenu, elementoClickeado) {
      

      const todasLasPantallas = document.querySelectorAll('.pantalla');
      todasLasPantallas.forEach(pantalla => {
          pantalla.classList.remove('pantalla-activa');
      });

      const idSeccion = 'seccion-' + seccionMenu;
      const pantallaMostrar = document.getElementById(idSeccion);
      
      if (pantallaMostrar) {
          pantallaMostrar.classList.add('pantalla-activa');
      }

      const todosLosEnlaces = document.querySelectorAll('.menu-link');
      todosLosEnlaces.forEach(enlace => {
          enlace.classList.remove('activo'); 
      });
      
      if (elementoClickeado) {
          elementoClickeado.classList.add('activo');
      }
      
      window.scrollTo({ top: 0, behavior: 'smooth' });
  }
 const elementosAnimar = document.querySelectorAll(".reveal-up");

function animarScroll() {
    elementosAnimar.forEach((elemento) => {
        const alturaVentana = window.innerHeight;
        const topeElemento = elemento.getBoundingClientRect().top;
        const puntoRevelado = 50; // Qué tan pronto aparece

        if (topeElemento < alturaVentana - puntoRevelado) {
            elemento.classList.add("active");
        }
    });
}

window.addEventListener("scroll", animarScroll);
window.addEventListener("load", animarScroll); 
// --- FUNCIONALIDAD DEL BUSCADOR Y FILTRO DE LA TABLA ---
const buscador = document.getElementById("buscador-tabla");
const filtroTipo = document.getElementById("filtro-tipo");
const filasTabla = document.querySelectorAll("#miTabla tbody tr");

function filtrarTabla() {
    const textoBusqueda = buscador.value.toLowerCase();
    const tipoSeleccionado = filtroTipo.value;

    filasTabla.forEach(fila => {
        const textoFila = fila.textContent.toLowerCase();
        // El tipo suele estar en la columna 4 (índice 3)
        const tipoFila = fila.cells[3].textContent.trim(); 

        const coincideTexto = textoFila.includes(textoBusqueda);
        const coincideTipo = (tipoSeleccionado === "Todos") || (tipoFila === tipoSeleccionado);

        if (coincideTexto && coincideTipo) {
            fila.style.display = ""; // Mostrar
        } else {
            fila.style.display = "none"; // Ocultar
        }
    });
}

if (buscador && filtroTipo) {
    buscador.addEventListener("keyup", filtrarTabla);
    filtroTipo.addEventListener("change", filtrarTabla);
}