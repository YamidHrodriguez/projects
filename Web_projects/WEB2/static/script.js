const circle = document.querySelector(".circle");
const video = document.getElementById("video");
const image = document.getElementById("image");
const body = document.body; // Selecciona el elemento body
const h1 = document.getElementById("tit");
const lightbul= document.querySelector(".lightbulb");
const icon=document.querySelector(".social");
let isVideoMode = false;
const yo = document.getElementById("yo");
// Ocultar el video al principio
video.style.display = "none";

function cambiarModo() {
    circle.style.opacity = "1";
    if (isVideoMode) {
        // Cambiar a modo imagen
        body.style.backgroundImage = "url('https://1.bp.blogspot.com/-B42E0UkiV-M/XSnjZjdhKSI/AAAAAAAAL4o/fy2J6fXSl98WbtMYbAklhtw3ss2xODx5ACLcBGAs/s1600/Paisaje-refelejo-naturaleza-2.gif')";
        video.style.display = "none";
        image.style.display = "block";
        
    } else {
        // Cambiar a modo video
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                h1.style.display = "none";
                circle.style.marginTop="-8%";
                circle.style.width = "360px";
                circle.style.height = "360px";
                body.style.backgroundImage = "url('https://1.bp.blogspot.com/-B42E0UkiV-M/XSnjZjdhKSI/AAAAAAAAL4o/fy2J6fXSl98WbtMYbAklhtw3ss2xODx5ACLcBGAs/s1600/Paisaje-refelejo-naturaleza-2.gif')";
                video.style.display = "block";
                image.style.display = "none";
                video.srcObject = stream;

            })
            .catch(function(err) {
                console.error("No se pudo acceder a la cámara: ", err);
            });
    }

    // Alternar el modo
    isVideoMode = !isVideoMode;

    // Quitar el controlador de eventos después de ejecutarlo una vez
    circle.removeEventListener("click", cambiarModo);
}

circle.addEventListener("contextmenu", () => {
    circle.style.opacity = "0.9";
});

circle.addEventListener("click", cambiarModo);



const icons = document.querySelectorAll(".icon");
const infoContainer = document.querySelector(".info-container");
const infoText = document.querySelector(".info-text");

icons.forEach(icon => {
    icon.addEventListener("click", function() {
        infoText.textContent = `${this.getAttribute("data-network")}`;
        infoContainer.style.display = "block";
        infoContainer.style.backgroundColor = "black";
        infoContainer.style.color="white";
        infoContainer.style.padding="1%";
        lightbul.style.width="55px";
        lightbul.style.height="55px";
        circle.style.marginBottom="-5%";
        lightbul.style.marginTop="-5%";
        icon.style.marginBottom="2%";
    });
});

document.addEventListener("click", function(event) {
    let clickedOnIcon = false;

    icons.forEach(icon => {
        if (icon.contains(event.target)) {
            clickedOnIcon = true;
        }
    });

    if (!infoContainer.contains(event.target) && !clickedOnIcon) {
        infoContainer.style.display = "none";
        lightbul.style.width="80px";
        lightbul.style.height="80px";

    }
});


const music = document.getElementById("background-music");
circle.addEventListener("contextmenu", () => {
    let state=true;
    if (state===true){
        music.play();
    }else{
        console.log("Error")
    }
})

