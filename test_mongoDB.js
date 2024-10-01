const { MongoClient } = require('mongodb');

// Reemplaza con tu cadena de conexión URI
const uri = 'mongodb+srv://gmvsvw2014:Rm5AaJCqCzkdMTcF@cluster0.9gi8h.mongodb.net/';

const client = new MongoClient(uri);

async function run() {
  try {
    // Conectar al cliente MongoDB
    await client.connect();

    console.log('Conectado a MongoDB');

    // Realiza operaciones en tu base de datos aquí...
    
  } finally {
    // Cerrar la conexión con MongoDB al finalizar
    await client.close();
  }
}

run().catch(console.dir);