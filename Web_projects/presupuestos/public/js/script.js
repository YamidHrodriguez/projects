
// Obtener referencias a elementos HTML
var incomesBtn = document.getElementById('income');
var egressBtn = document.getElementById('egress');
var buyBtn = document.getElementById('buy');
var reportBtn = document.getElementById('report');
var debtBtn = document.getElementById('debt');
var miMain = document.querySelector('main');
//leer archivo CSV registros de data

// Variable para almacenar el contenido original de miMain
var contenidoOriginal = miMain.innerHTML;

// Función para cancelar y volver al menú principal
function volverAlMenuPrincipal() {
    miMain.innerHTML = contenidoOriginal;
}

function obtenerDatos() {
    fetch('/obtener-datos')
    .then(response => response.json())
    .then(data => {
        console.log(data); // Aquí tendrás acceso a los datos en formato JSON
        // Puedes realizar cualquier otra acción que desees con los datos
    })
}
//   .catch(error => console.error('Error al realizar la solicitud:', error));

//     fetch('/obtener-datos')
//       .then(response => response.json())
//       .then(data => {
//         // Limpiar las secciones antes de agregar nuevos datos
//         document.getElementById('income-content').innerHTML = '';
//         document.getElementById('egress-content').innerHTML = '';
//         document.getElementById('debt-content').innerHTML = '';
//         document.getElementById('buy-content').innerHTML = '';

//         // Iterar sobre los datos y agregarlos a las secciones correspondientes
//         data.forEach(item => {
//             const sectionId = item.type === 'Ing' ? 'income-content' :
//                               item.type === 'Egr' ? 'egress-content' :
//                               item.type === 'Pag' ? 'debt-content' :
//                               item.type === 'Com' ? 'buy-content' : '';

//             if (sectionId !== '') {
//                 const section = document.getElementById(sectionId);
//                 const newItem = document.createElement('div');
//                 newItem.textContent = `${item.description}: $${item.amount} - ${item.date}`;
//                 section.appendChild(newItem);
//             }
//         });

//         // Almacena los datos en el almacenamiento local
//         localStorage.setItem('cachedData', JSON.stringify(data));
//       })
//       .catch(error => console.error('Error al obtener datos:', error));
// }

// Al cargar la página, intenta mostrar los datos almacenados localmente
document.addEventListener('DOMContentLoaded', () => {
    const cachedDataString = localStorage.getItem('cachedData');

    if (cachedDataString) {
      const cachedData = JSON.parse(cachedDataString);
      const resultadoDiv = document.getElementById('resultado');
      resultadoDiv.innerHTML = JSON.stringify(cachedData, null, 2);
    }
});
// Agregar un event listener al contenedor principal (miMain) utilizando delegación de eventos
miMain.addEventListener('click', function (event) {
    var target = event.target;

    // Verificar si el clic se hizo en el botón "Cancelar"
    if (target.id === 'cancel') {
        volverAlMenuPrincipal();
    }

    function showSection(buttonId, sectionColor, formAction, formTitle, inputType,type) {
        miMain.innerHTML = `
            <style>
                #${buttonId}-section{
                    background-color: ${sectionColor};
                }
                main {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: #8f8f8f;
                }
                main .menu {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    background-color: #8f8f8f;
                    color: #fff;
                    font-family: Arial, sans-serif;
                    font-size: 16px;
                    line-height: 1.5;
                    text-align: center;
                    padding: 20px;
                    box-sizing: border-box;
                    border: 1px solid #fff;
                    border-radius: 10px;
                    width: 100%;
                    height: 100%;
                    flex-wrap: wrap;
                }
                form {
                    background-color: #8f8f8f;
                    margin-top: -30px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    width: 100%;
                    height: 100%;
                    padding: 0;
                    box-sizing: border-box;
                }
                form h1 {
                    margin-bottom: 20px;
                    font-size: 24px;
                    font-weight: bold;
                    text-transform: uppercase;
                    color: #fff;
                }
                form div:not(:last-child) {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    border: 1px solid #fff;
                    width: 80%;
                    height: 70px;
                    margin-bottom: 10px;
                }
                #${buttonId}-input {
                    width: 80%;
                    height: 70px;
                    border: none;
                }
                #cancel-input, #cancel-pago-input {
                    width: 80%;
                    height: 70px;
                    border: none;
                }
                input[type="submit"], input[type="button"] {
                    width: 100%;
                    height: 100%;
                    border-radius: 5px;
                    padding: 10px;
                    box-sizing: border-box;
                    font-size: 16px;
                    line-height: 1.5;
                    text-align: center;
                    color: #fff;
                    cursor: pointer;
                    margin-bottom: 2%;
                }
                #cancel-input input, #cancel-pago-input input {
                    width: 100%;
                    height: 100%;
                    border: none;
                    border-radius: 5px;
                    padding: 10px;
                    box-sizing: border-box;
                    font-size: 16px;
                    line-height: 1.5;
                    text-align: center;
                    cursor: pointer;
                }
                #cancel-input input {
                    background-color: red;
                    margin-bottom: 4%;
                }
                #cancel-pago-input input {
                    background-color: red;
                }
                #cancel-input input:hover, #cancel-pago-input input:hover {
                    background-color: darkred;
                }
                #${buttonId}-input input {
                    background-color: ${inputType};
                    border: ${inputType};
                }
                #${buttonId}-input input:hover {
                    background-color: dark${inputType};
                }
            </style>
            <div class="menu">
                <form action="${formAction}" method="post">
                    <h1>${formTitle}</h1>
                    <div>
                        <label for="description">${formTitle === 'Compras por hacer' ? 'Descripción' : 'Descripción'} </label>
                        <input type="text" name="description${type}" id="description${type}">
                    </div>
                    <div>
                        <label for="amount">${formTitle === 'Compras por hacer' ? 'Monto en $' : 'Monto en $'}</label>
                        <input type="number" name="amount${type}" id="amount${type}" placeholder="$">
                    </div>
                    <div>
                        <label for="date">${formTitle === 'Compras por hacer' ? 'Fecha' : 'Fecha'}</label>
                        <input type="date" name="date${type}" id="date${type}">
                    </div>
                    <div id="type-input" style="display: none;">
                        <label for="type">Tipo de ${formTitle === 'Presupuestos' ? 'ingreso' : 'egreso'}</label>
                        <input type="text" name="type" id="type" value="${inputType}">
                    </div>
                    <div id="${buttonId}-input">
                        <input type="submit" onclick="obtenerDatos()" value="Confirmar">
                    </div>
                    <div id="cancel-pago-input">
                        <input type="button" value="${formTitle === 'Pagos a realizar' ? 'Cancelar pago' : 'Cancelar'}" id="cancelar">
                    </div>
                    <div id="cancel-input">
                        <input type="button" value="Cancelar" id="cancel">
                    </div>
                </form>
            </div>
        `;
        // Después de mostrar el formulario, también llamamos a obtenerDatos
        obtenerDatos();
    }
    
    // Luego, puedes utilizar la función showSection en lugar de repetir el código para cada botón
    
    if (target.id === 'income') {
        showSection('income', 'green', '/procesar/ingresos', 'Ingresos', 'ingreso','Ing');
    }
    
    if (target.id === 'egress') {
        showSection('egress', 'rgb(163, 27, 6)', '/procesar/egresos', 'Egresos', 'egreso','Egr');
    }
    
    if (target.id === 'debt') {
        showSection('debt', 'rgb(222, 100, 0)', '/procesar/pagos', 'Pagos a realizar', 'pago','Pag');
    }
    
    if (target.id === 'buy') {
        showSection('buy', 'rgb(20, 20, 84)', '/procesar/compras', 'Compras por hacer', 'compra','Com');
    }   
});




