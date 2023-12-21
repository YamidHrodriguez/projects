const express = require('express');
const path = require('path'); // Módulo para trabajar con rutas de archivos
const app = express();
const port = 3000;
const fs = require('fs');
const bodyParser = require('body-parser');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

// Configurar el middleware para servir archivos estáticos desde la carpeta 'public'
app.use(express.static('public'));

// Establecer la carpeta de vistas
app.set('views', path.join(__dirname, 'views'));

// Configurar Express para servir archivos estáticos desde la carpeta 'data'
app.use('/data', express.static(path.join(__dirname, 'data')));

// Establecer el motor de vistas (opcional si usas un motor de plantillas como EJS o Pug)
app.set('view engine', 'html');

// Configurar middleware para analizar datos del formulario
app.use(bodyParser.urlencoded({ extended: true }));


// Ruta para la página principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
});

// Ruta para manejar el envío del formulario
app.post('/guardar', (req, res) => {
    // Obtener el valor del input desde la solicitud
    const name = req.body.name;
    const fecha = req.body.date;
    const pregunta = req.body.pregunta;
    // Guardar el nombre en un archivo CSV
    const csvFilePath = './data/archivo.csv';
    const csvWriter = createCsvWriter({
        path: csvFilePath,
        header: [
            { id: 'name', title: 'Nombre' },
            {id: 'fecha', title: 'Fecha de nacimiento'},
            {id: 'pregunta', title: 'Pregunta'}
        ],
        append: true, // Habilitar modo de anexar para agregar líneas al final del archivo
    });
    
    // Datos para agregar
    const dataToAdd = [
        { name: name, fecha: fecha, pregunta: pregunta }
    ];
    // Escribir datos en el archivo CSV
    csvWriter.writeRecords(dataToAdd)
        .then(() => {
            console.log('Nombre y fecha agregado con éxito al archivo CSV.');
            res.redirect('/resultados');
        })
        .catch((err) => {
            console.error('Error al agregar nombre al archivo CSV:', err);
            res.status(500).send('Error interno del servidor');
        });
});

// Nueva ruta para mostrar resultados
app.get('/resultados', (req, res) => {
    // Aquí puedes renderizar la página con los resultados o registros
    res.sendFile(path.join(__dirname, 'views', 'registros.html'));
});

app.get('/formatear_registros', (req, res) => {
    const fs = require('fs/promises');

    async function eliminarTodosLosRegistros(ruta) {
        try {
            // Crear un archivo vacío para eliminar todos los registros
            await fs.writeFile(ruta, '');

            console.log('Todos los registros han sido eliminados con éxito.');
            res.sendFile(path.join(__dirname, 'views', 'index.html'));
        } catch (error) {
            console.error('Error al eliminar todos los registros:', error);
            throw error;
        }
    }

    // Ejemplo de uso
    const rutaCSV = 'data/archivo.csv';

    eliminarTodosLosRegistros(rutaCSV);
});