const express = require('express');
const path = require('path'); // Módulo para trabajar con rutas de archivos
const app = express();
const csv = require('csv-parser');
const port = 3333;
const fs = require('fs');
const bodyParser = require('body-parser');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const mysql = require('mysql');

// Configura la conexión
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'nidian56',
  database: 'presupuesto'
});

// Conéctate a la base de datos
connection.connect((err) => {
  if (err) {
    console.error('Error al conectar a MySQL:', err);
  } else {
    console.log('Conexión exitosa a MySQL');
    
    // connection.end((err) => {
    //   if (err) {
    //     console.error('Error al cerrar la conexión:', err);
    //   } else {
    //     console.log('Conexión cerrada exitosamente');
    //   }
    // });

    // Ahora puedes realizar consultas
  }
});

// Variable para almacenar datos en caché
let cachedData = null;



function registrarDB(id,tabla,tipe,dataToAdd,res) {
  // Realizar la consulta de inserción
  const sql = `INSERT INTO ${tabla} (Id_${tipe}, Description_${tipe}, Amount_${tipe}, Date_${tipe}) VALUES (?, ?, ?, ?)`;
  const values = [id, dataToAdd.description, dataToAdd.amount, dataToAdd.date];

  connection.query(sql, values, (error, results) => {
    if (error) {
      console.error('Error al insertar en la base de datos:', error);
      res.status(500).send('Error interno del servidor');
    } else {
      console.log('Registro agregado a la base de datos con éxito');
      return res.redirect("/");
    }
  });

  // const query = `SELECT * FROM ${tabla}`;

  // connection.query(query, (error, results, fields) => {
  //   if (error) {
  //     console.error('Error en la consulta:', error);
  //     // Manejar el error y enviar una respuesta al cliente si es necesario
  //   } else {
  //     // Verificar si hay resultados antes de acceder a las propiedades
  //     if (results.length > 0) {
  //       // Acceder a la primera fila y la propiedad específica (en este caso, "Description_${tipe}")
  //       const valorCelda = results;
  //       console.log(valorCelda);

  //       // Aquí podrías renderizar tu página HTML o enviar el valor de otra manera
  //     } else {
  //       console.log('No se encontraron resultados en la consulta.');
  //     }
  //   }
  // });

}


function registrarCSV(dataToAdd,res){
  // Definir la ruta del archivo CSV
  const csvFilePath = path.join(__dirname, 'data', 'registros.csv');

  const csvWriter = createCsvWriter({
    path: csvFilePath,
    header: [
        { id: 'description', title: 'Descripción' },
        { id: 'amount', title: 'Monto' },
        { id: 'date', title: 'Fecha' },
        { id: 'type', title: 'Tipo' }
    ],
    append: true  // Permite agregar al final del archivo existente
  });

// Escribir el nuevo registro en el archivo CSV
  csvWriter.writeRecords([dataToAdd])
    .then(() => {
        console.log('Registro agregado con éxito');
    })
    .catch((error) => {
        console.error('Error al agregar el registro', error);
        res.status(500).send('Error interno del servidor');
    });
}

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


// Ruta para manejar el envío del formulario /ingresos
app.post('/procesar/ingresos', (req, res) => {
  // Obtener el valor del input desde la solicitud
  const descriptionIng = req.body.descriptionIng;
  const amountIng = req.body.amountIng;
  const dateIng = req.body.dateIng;
  const type = req.body.type;

  const dataToAdd = {
    description: descriptionIng,
    amount: amountIng,
    date: dateIng
  }

  // Log de los datos para verificar
  console.log(req.body, dataToAdd);
  
  registrarCSV(dataToAdd,res);
  registrarDB(0,"Income","income",dataToAdd, res);
});

app.post('/procesar/egresos', (req, res) => {
  // Obtener el valor del input desde la solicitud
  const descriptionEgr = req.body.descriptionEgr;
  const amountEgr = req.body.amountEgr;
  const dateEgr= req.body.dateEgr;
  const type= req.body.type;
  const dataToAdd = {
    description: descriptionEgr,
    amount: amountEgr,
    date: dateEgr,
    type: type
  }
  
  console.log(req.body, dataToAdd);
  registrarCSV(dataToAdd,res);
  registrarDB(0,"Egress","egress",dataToAdd, res);
});

app.post('/procesar/pagos', (req, res) => {
  // Obtener el valor del input desde la solicitud
  const descriptionPag = req.body.descriptionPag;
  const amountPag = req.body.amountPag;
  const datePag = req.body.datePag;
  const type= req.body.type;
  const dataToAdd = {
    description: descriptionPag,
    amount: amountPag,
    date: datePag

  }
  console.log(req.body, dataToAdd);
  
  registrarCSV(dataToAdd,res);
  registrarDB(0,"Debt","debt",dataToAdd, res);
});
app.post('/procesar/compras', (req, res) => {
  // Obtener el valor del input desde la solicitud
  const descriptionCom = req.body.descriptionCom;
  const amountCom = req.body.amountCom;
  const dateCom = req.body.dateCom;
  const type= req.body.type;
  const dataToAdd = {
    description: descriptionCom,
    amount: amountCom,
    date: dateCom
  }
  console.log(req.body, dataToAdd);
  
  registrarCSV(dataToAdd,res);
  registrarDB(0,"Buy","buy",dataToAdd, res);
})

app.get('/obtener-datos', (req, res) => {
  // Realizar una consulta SQL para obtener todos los datos
  const query = 'SELECT * FROM Income UNION SELECT * FROM Egress UNION SELECT * FROM Debt UNION SELECT * FROM Buy';

  connection.query(query, (error, results, fields) => {
    if (error) {
      console.error('Error en la consulta:', error);
      res.status(500).send('Error interno del servidor');
    } else {
      res.json(results);
    }
  });
});

// // Ruta para obtener datos de ingresos
// app.get('/obtener-ingresos', (req, res) => {
//   const query = 'SELECT * FROM Income';
  
//   connection.query(query, (error, results, fields) => {
//     if (error) {
//       console.error('Error en la consulta de ingresos:', error);
//       res.status(500).send('Error interno del servidor');
//     } else {
//       res.json(results);
//     }
//   });
// });

// // Ruta para obtener datos de egresos
// app.get('/obtener-egresos', (req, res) => {
//   const query = 'SELECT * FROM Egress';
  
//   connection.query(query, (error, results, fields) => {
//     if (error) {
//       console.error('Error en la consulta de egresos:', error);
//       res.status(500).send('Error interno del servidor');
//     } else {
//       res.json(results);
//     }
//   });
// });

// // Ruta para obtener datos de pagos
// app.get('/obtener-pagos', (req, res) => {
//   const query = 'SELECT * FROM Debt';
  
//   connection.query(query, (error, results, fields) => {
//     if (error) {
//       console.error('Error en la consulta de pagos:', error);
//       res.status(500).send('Error interno del servidor');
//     } else {
//       res.json(results);
//     }
//   });
// });

// // Ruta para obtener datos de compras
// app.get('/obtener-compras', (req, res) => {
//   const query = 'SELECT * FROM Buy';
  
//   connection.query(query, (error, results, fields) => {
//     if (error) {
//       console.error('Error en la consulta de compras:', error);
//       res.status(500).send('Error interno del servidor');
//     } else {
//       res.json(results);
//     }
//   });
// });
