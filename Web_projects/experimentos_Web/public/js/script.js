// Para el ejemplo, asumiré que tienes un servidor en http://localhost:3000
const baseURL = 'http://localhost:3000';

// Función para hacer una solicitud y mostrar la respuesta en la consola
function obtenerDatosYMostrar(url) {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);

      // Aquí puedes procesar los datos y mostrarlos en tu interfaz de usuario
    })
    .catch(error => console.error('Error al obtener datos:', error));
}

// Obtener y mostrar datos de cada endpoint
obtenerDatosYMostrar(`${baseURL}/usuarios`);
obtenerDatosYMostrar(`${baseURL}/ingresos`);
obtenerDatosYMostrar(`${baseURL}/egresos`);
obtenerDatosYMostrar(`${baseURL}/informes`);
