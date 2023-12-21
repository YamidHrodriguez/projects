console.log("Hola mundo")
const btn = document.getElementById('btn');
const videoContainer = document.getElementById('video-container'); 
const main = document.querySelector('main');
function abrirVideo(){
    // Obtener el elemento de video, el contenedor y el botón
    const videoElement = document.getElementById('video-stream');
    const main = document.querySelector('main');
    const stopButton = document.getElementById('stopButton');

    let stream; // Variable para almacenar el objeto del flujo de la cámara

    // Verificar si el navegador admite la API de medios
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Solicitar acceso a la cámara
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (cameraStream) {
                // Asignar el flujo de la cámara al elemento de video
                videoElement.srcObject = cameraStream;
                stream = cameraStream; // Almacenar el objeto del flujo de la cámara

                // Manejar clic en el botón de detener
                main.addEventListener('click', function () {
                    // Detener la transmisión de la cálculadora
                    const tracks = stream.getTracks();
                    tracks.forEach(track => track.stop());
                    //no quites el background de mi imagen
                    videoElement.srcObject = null;
                    stream = null;
                    
                })
                stopButton.addEventListener('click', function () {
                    // Detener la transmisión de la cámara
                    const tracks = cameraStream.getTracks();
                    tracks.forEach(track => track.stop());

                    // Limpiar el objeto del flujo
                    videoElement.srcObject = null;
                    stream = null;
                });
            })
            .catch(function (error) {
                console.error('Error al acceder a la cámara:', error);
            });
    } else {
        console.error('La API de medios no está soportada en este navegador');
    }
}

function reproducirAudio() {
    var miSonido = document.getElementById('miSonido');
    miSonido.play();
    // También puedes ocultar el elemento "reproducirAudio" si lo deseas
    document.getElementById('reproducirAudio').style.display = 'none';
}
function detenerAudio() {
    var miSonido = document.getElementById('miSonido');
    miSonido.pause();
    miSonido.currentTime = 0; // Reinicia la reproducción al principio del audio
}



btn.addEventListener('click', abrirVideo); 
videoContainer.addEventListener('click', abrirVideo);
