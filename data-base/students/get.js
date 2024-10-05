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
    const collection = database.collection('students register'); // Colección "teachers register"

    // **Leer Todos los Documentos**
    // Ejemplo: obtener todos los documentos de la colección
    const allDocs = await collection.find({}).toArray();
    console.log('Todos los documentos:', JSON.stringify(allDocs, null, 2));

    // **Leer Documentos con un Filtro**
    // Ejemplo: obtener documentos donde el campo 'Estado' sea 'Activo'
    const activeTeachers = await collection.find({ Matrícula: '1028975' }).toArray();
    console.log('Alumnos activos:', JSON.stringify(activeTeachers, null, 2));

    // Ejemplo: obtener un solo documento donde el campo 'Nombre' sea 'Dr. Juan Pérez'
    const singleDoc = await collection.findOne({ Asignatura: 'Sistemas Operativos' });
    console.log('Documento encontrado:', JSON.stringify(singleDoc, null, 2));

  } catch (err) {
    console.error('Error al conectar a MongoDB:', err);
  } finally {
    // Cerrar la conexión con MongoDB
    await client.close();
  }
}

run().catch(console.dir);
