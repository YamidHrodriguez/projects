<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yamid Tarot en vivo</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body class="body2" style="margin:0;padding:0;box-sizing:border-box;">
    <script>

        function Check(nombreCompleto) {
            var x = prompt("Ingrese el número de las cartas: ");
            
            const title = document.createElement("h1");
            title.textContent = "Respuesta del Tarot a " + nombreCompleto;
            title.style.alignContent = "center";
            title.style.display="flex-box";
            title.style.fontSize="1.8rem";
            const text_container= document.createElement("div");
            
            
            const container3 = document.createElement("div");
            container3.classList.add('mi-contenedor-estilo');
            const cardNumbers = x.split(",").map(Number);
            const uniqueCardNumbers = [];
            let hasError = false;
            
            container3.appendChild(title);
            const container4=document.createElement("div");
            container3.appendChild(container4);

            for (const number of cardNumbers) {
                if (number >= 0 && number <= 22) {
                    if (uniqueCardNumbers.includes(number)) {
                        hasError = true;
                        break; // Sal del bucle si hay una repetición
                    } else {
                        uniqueCardNumbers.push(number);
                        const imagen = document.createElement("img");
                        imagen.src = `./images/tarot_marsella/tarot_${number}.jpg`; // Reemplaza 'ruta/a/tu/imagen' por la ubicación real de tus imágenes.
                        imagen.alt = `Arcano ${number}`;
                        container4.appendChild(imagen);
                    }
                }
            }

            if (hasError) {
                alert("Error: Se han ingresado cartas repetidas.");
                return; // Detén la ejecución si hay un error
            }

            // Agregar el contenido al contenedor
            
            // Agregar el contenedor a la página
            container4.style.display="flex";
            container4.style.justifyContent="space-between"
            const contenedor = document.getElementById("container2");
            contenedor.appendChild(container3);
        }
    </script>
    <header class="header" style="background: #0D0D0D; width:100%;height:100px;margin-top:-5px; padding-left:15px;">
        <h1 style="padding:2%;width:40%">DINAMICA DE TAROT EN VIVO</h1>
        <h1 class="titulo-2" id="tarotTitle">TAROT EN VIVO 🔴</h1>
        <script>
            const tarotTitle = document.getElementById('tarotTitle');
            let isEncendido = true;

            // Función para alternar el estado del título
            function alternarTextoTitulo() {
                isEncendido = !isEncendido;

                if (isEncendido) {
                    tarotTitle.innerText = 'TAROT EN VIVO 🔴';
                } else {
                    tarotTitle.innerText = 'TAROT EN VIVO ⚪';
                }
            }

            // Encender el título inicialmente
            alternarTextoTitulo();

            // Configurar un intervalo para alternar el estado cada 1000 milisegundos (1 segundo)
            setInterval(alternarTextoTitulo, 1000);
        </script><br><br>
        <p id="datetime2"><span id="fechaYHora2"></span><br>Colombia</p>

        <script>
            // Aquí se agregará la fecha y hora actual
            var fechaYHoraElemento = document.getElementById("fechaYHora2");
            
            // Función para actualizar la fecha y hora
            function actualizarFechaYHora() {
                var fechaHoraActual = new Date();
                fechaYHoraElemento.innerHTML = fechaHoraActual.toLocaleString();
            }

            // Actualiza la fecha y hora cada segundo
            setInterval(actualizarFechaYHora, 1000);

            // Llama a la función para mostrar la fecha y hora inicial
            actualizarFechaYHora();
        </script>
    </header>
    
    <div id="container2">
        <?php
          include("conection.php");
          $sql = "SELECT * FROM participantes";
          $result = $conexion->query($sql);
          
          // Mostrar los datos en una tabla HTML
          echo "<table>";
          echo "<tr><th>ID</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Pregunta</th><th>¿Listo?</th></tr>";
          
          if ($result->num_rows > 0) {
              while ($row = $result->fetch_assoc()) {
                  echo "<tr><td>" . $row["id"] . "</td><td>" . $row["nombre_completo"] . "</td><td>" . $row["fecha_nacimiento"] . "</td><td>" . $row["pregunta_concreta"] . "</td><td>" . "<input type='checkbox' onclick='Check(\"" . $row["nombre_completo"] . "\")'>" . "</td><</tr>";
              }
          } else {
              echo "";
          }
        ?>
        <section class="botons-2">
            <form method="post" action="procesar_info_2.php" class="botones">
                <input type="submit" id="delete" name="delete" value="Borrar">
                <input type="submit" id="new" name="new" value="Nuevo">
            </form>
        </section>
    </div>
</body>
</html>