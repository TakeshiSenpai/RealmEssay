const { MongoClient } = require('mongodb');

// URI de conexión a MongoDB (asegúrate de reemplazarlo con el tuyo)
const uri = 'mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0';
const client = new MongoClient(uri);

async function run() {
  try {
    // Conectar a MongoDB
    await client.connect();
    console.log('Conectado a MongoDB correctamente');

    // Seleccionar la base de datos y colección
    const database = client.db('ChatbotDB'); // Reemplaza con el nombre de tu base de datos
    const collection = database.collection('teachers register'); // Colección "teachers register"

    // **Actualizar un Solo Documento**
    // Ejemplo: actualizar el 'Email' del documento donde 'Nombre' sea 'Dr. Juan Pérez'
    const filter = { Nombre: 'Dr. Juan Pérez' }; // Criterio de búsqueda para encontrar el documento
    const updateDoc = {
      $set: {
        Email: 'juan.perez.actualizado@uabc.edu.mx', // Nuevo valor para el campo 'Email'
      },
    };

    const result = await collection.updateOne(filter, updateDoc);
    console.log(`Documentos actualizados: ${result.modifiedCount}`);
  } catch (err) {
    console.error('Error al conectar a MongoDB:', err);
  } finally {
    // Cerrar la conexión con MongoDB
    await client.close();
  }
}

run().catch(console.dir);
