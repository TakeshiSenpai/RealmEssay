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

    // Mostrar documentos que coinciden antes de eliminar
    const docsToDeleteOne = await collection.find({ Nombre: 'Dr. Juan Pérez' }).toArray();
    console.log('Documentos que coinciden con deleteOne:', docsToDeleteOne);

    const docsToDeleteMany = await collection.find({ Estado: 'Inactivo' }).toArray();
    console.log('Documentos que coinciden con deleteMany:', docsToDeleteMany);

    // **Eliminar un Solo Documento**
    // Ejemplo: eliminar un documento donde el campo 'Nombre' sea 'Dr. Juan Pérez'
    const deleteResultOne = await collection.deleteOne({ Nombre: 'Dr. Juan Pérez' });
    console.log(`Documentos eliminados: ${deleteResultOne.deletedCount}`);

    // **Eliminar Múltiples Documentos**
    // Ejemplo: eliminar todos los documentos donde el campo 'Estado' sea 'Inactivo'
    const deleteResultMany = await collection.deleteMany({ Estado: 'Inactivo' });
    console.log(`Documentos eliminados: ${deleteResultMany.deletedCount}`);
  } catch (err) {
    console.error('Error al conectar a MongoDB:', err);
  } finally {
    // Cerrar la conexión con MongoDB
    await client.close();
  }
}

run().catch(console.dir);
