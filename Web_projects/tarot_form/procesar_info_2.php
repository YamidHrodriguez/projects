<?php
// Incluir el archivo de configuración
include('conection.php');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Verificar si se ha enviado un formulario

    if (isset($_POST['delete'])) {
      $query="DELETE FROM participantes";
      if ($conexion->query($query) === TRUE) {
            // Reiniciar la secuencia de autoincremento
            $reset_auto_increment_query = "ALTER TABLE participantes AUTO_INCREMENT = 1";
            if ($conexion->query($reset_auto_increment_query) === TRUE) {
                echo "<script>alert('Los registros han sido eliminados y el índice ha sido reiniciado.')</script>";
            } else {
                echo "<script>alert('Error al reiniciar el índice: " . $conexion->error . "')</script>";
            }
            header('Location: index.php');
            exit;
        } else {
            echo "<script>alert(Error al eliminar registros: " . $conexion->error . ")</script>";
        };
    } elseif (isset($_POST['new'])) {
        header('Location: index.php');
        exit;
    }
    }else {
        echo "<script>alert('No se ha seleccionado un botón válido.')</script>";
    }

// Cerrar la conexión
$conexion->close();
?>