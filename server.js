const express = require('express');
const path = require('path');
const cors = require('cors');
const serveIndex = require('serve-index');
const helmet = require('helmet');

const app = express();

// Enable CORS
app.use(cors());

// Add security headers for SharedArrayBuffer
app.use(helmet());
app.use((req, res, next) => {
  res.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
  res.setHeader('Cross-Origin-Embedder-Policy', 'require-corp');
  next();
});

// Serve static files and enable directory listing for /images
const imagesPath = path.join(__dirname, 'src/resources/imagenes');
app.use(
  '/images',
  express.static(imagesPath),
  serveIndex(imagesPath, { icons: true, view: 'details' }) // Enable file listing with icons and detailed view
);

// Start the server on port 3000
app.listen(3000, () => {
  console.log('Servidor corriendo en http://192.168.1.100:3000');
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Error en el servidor');
});
