// Para el ejemplo, asumiré que tienes un servidor en http://localhost:3000
const baseURL = 'http://localhost:3000';
const btnConsultar = document.getElementById('btn-consultar');

btnConsultar.addEventListener('click', () => {
    obtenerDatosYMostrar(`${baseURL}/usuarios`);
});

// Función para hacer una solicitud y mostrar la respuesta en la consola
function obtenerDatosYMostrar(url) {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Aquí puedes procesar los datos y mostrarlos en tu interfaz de usuario 
      construirTabla(data);
      setInterval(() => {
        destruirTabla();
        if (destruirTabla()) {
            window.location.href = "/";
        }
    
      }, 5000);

      
    })
    .catch(error => console.error('Error al obtener datos:', error));
}


function construirTabla(data) {
    // Seleccionar el contenedor de la tabla
    const tablaContainer = document.getElementById('signUp');

    // Crear la tabla
    const tabla = document.createElement('table');
    tabla.border = '1';
    

    // Crear la fila de encabezado
    const encabezado = document.createElement('tr');
    for (const key in data[0]) {
      console.log(key);
      const th = document.createElement('th');
      th.textContent = key;
      encabezado.appendChild(th);
    }
    tabla.appendChild(encabezado);

    // Crear filas de datos
    data.forEach(item => {
      const fila = document.createElement('tr');
      for (const key in item) {
        const td = document.createElement('td');
        td.textContent = item[key];
        fila.appendChild(td);
      }
      tabla.appendChild(fila);
    });
 
    // Limpiar el contenedor y agregar la tabla
    tablaContainer.innerHTML = '';
    tablaContainer.appendChild(tabla);
  }

  function destruirTabla() {
    const tablaContainer = document.getElementById('signUp');
    tablaContainer.innerHTML = '';
    console.log('Se ha destruido la tabla');
    // volver a los valores de antes de consultar
    return true;
}
