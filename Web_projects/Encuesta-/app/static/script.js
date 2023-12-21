// script.js
document.addEventListener('DOMContentLoaded', function () {
    // Desactivar la funcionalidad de retroceso
    history.pushState(null, null, document.URL);
    window.addEventListener('popstate', function () {
        history.pushState(null, null, document.URL);
    });

    // Función para actualizar el fondo con el degradado
    function actualizarDegradado() {
        // Obtener los valores de los inputs
        var valor1 = parseFloat(document.getElementById('input1').value);
        var valor2 = parseFloat(document.getElementById('input2').value);

        // Calcular los porcentajes
        var porcentaje1 = (valor1 / (valor1 + valor2)) * 100;
        var porcentaje2 = (valor2 / (valor1 + valor2)) * 100;

        // Modificar los colores en función de los porcentajes
        var color1 = '#00bf66';
        var color2 = '#2a2a2a';

        // Ajustar los colores según los porcentajes
        if (porcentaje1 > porcentaje2) {
            color1 = '#2a2a2a';
            color2 = '#00bf66';
        }

        // Aplicar los colores al fondo con los porcentajes actualizados
        document.querySelector('.list-e').style.background = `linear-gradient(${color1} 0% ${porcentaje1}%, ${color2} ${porcentaje1}% ${porcentaje1 + porcentaje2}%)`;

        
    }

    // Asociar la función al botón
    document.querySelector('button').addEventListener('click', actualizarDegradado);
});
