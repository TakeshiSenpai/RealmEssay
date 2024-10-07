const { MongoClient } = require('mongodb');
const fs = require('fs'); // Módulo para leer el archivo JSON

// URI de conexión a MongoDB (remplazar por "usuario:contraseña")
const uri = 'mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0';
const client = new MongoClient(uri);

async function run() {
  try {
    // Conectar a MongoDB
    await client.connect();
    console.log('Conectado a MongoDB correctamente');

    // Leer el archivo JSON
    const jsonData = JSON.parse(fs.readFileSync('data.json', 'utf8'));
    console.log('Archivo JSON leído correctamente:', jsonData);

    // Seleccionar la base de datos y colección
    const database = client.db('ChatbotDB'); // Reemplaza con el nombre de tu base de datos
    const collection = database.collection('teachers register');

    // Insertar el documento JSON en la colección 'chat'
    const result = await collection.insertOne(jsonData);
    console.log(`Documento insertado con ID: ${result.insertedId}`);
  } catch (err) {
    console.error('Error al conectar a MongoDB:', err);
  } finally {
    // Cerrar la conexión con MongoDB
    await client.close();
  }
}

run().catch(console.dir);
