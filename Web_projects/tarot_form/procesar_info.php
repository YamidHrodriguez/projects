<?php
// Incluir el archivo de configuración
include('conection.php');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Verificar si se ha enviado un formulario

    if (isset($_POST['env'])) {
        // Formulario de inserción
        if (isset($_POST['name'], $_POST['date'], $_POST['question'])) {
            $nombre = $_POST['name'];
            $nacimiento = $_POST['date'];
            $pregunta = $_POST['question'];
            $query = "INSERT INTO participantes (nombre_completo, fecha_nacimiento, pregunta_concreta) VALUES ('$nombre', '$nacimiento', '$pregunta')";
            if ($conexion->query($query) === TRUE) {
                header('Location: index.php');
                exit;
            } else {
                echo "Error al insertar en la base de datos: " . $conexion->error;
            }
        } else {
            echo "Faltan datos en el formulario.";
        }
    } elseif (isset($_POST['consult'])) {
        // Formulario de consulta
        header('Location: mostrar_info.php');
        exit;
    }
    }else {
        echo "No se ha seleccionado un botón válido.";
    }

// Cerrar la conexión
$conexion->close();
?>
