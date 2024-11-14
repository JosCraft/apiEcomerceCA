const express = require('express');
const path = require('path');
const cors = require('cors');
const serveIndex = require('serve-index');
const helmet = require('helmet');

const app = express();

// Habilitar CORS
app.use(cors());

// Añadir los encabezados de seguridad necesarios para SharedArrayBuffer
app.use(helmet());
app.use((req, res, next) => {
  res.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
  res.setHeader('Cross-Origin-Embedder-Policy', 'require-corp');
  next();
});

// Servir archivos estáticos y mostrar el índice del directorio
app.use('/images', express.static(path.join(__dirname, 'src/resources')), serveIndex(path.join(__dirname, 'UNITEL'), { icons: true }));

// Iniciar el servidor en el puerto 3000
app.listen(3000, () => {
  console.log('Servidor corriendo en http://192.168.1.100:3000');
});

// Manejo de errores
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Error en el servidor');
});
