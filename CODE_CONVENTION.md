# Convención de Código

En este proyecto se seguirán las siguientes convenciones de código para mantener un código limpio y legible. Por favor, lee este documento antes de comenzar o continuar a trabajar en el proyecto.

#### Por el Princeso Leonardo.

## Backend

En el backend, escrito en Python, seguiremos la convención **snake_case** para variables, funciones, archivos y carpetas, todo en minúsculas. Todo código debe estar escrito en inglés. Los comentarios de las funciones deben incluir un comentario superior en español que explique qué hace la función y cómo lo hace, especialmente si la función es compleja.

### Comentarios
- Los comentarios deben de estar en español, a menos que sea necesario usar un término técnico en inglés.
- Cada línea de comentario debe de tener un espacio después del símbolo `#`.
```python
# Do:
# Este es un comentario.
# Con muchas líneas comentario.

# Don't:
"""
Este es un comentario.
Con muchas líneas.
"""
```

### Funciones

- Usar snake_case para las funciones.
```python
def calculate_sum(variable_a, variable_b):
    return variable_a + variable_b
```

- Cada función debe de estar acompañado de un comentario que describa que hace la función, describir sus parámetros y, si es necesario, lo que regresa.
```python
# Esta función calcula la suma de dos variables.
# Params:
#   parameter_one: Parámetro uno de la función.
#   parameter_two: Parámetro dos de la función.
def complex_function(parameter_one, parameter_two):
   parameter_one.append(parameter_two)
```
- En caso de que la función no sea muy compleja, o si el nombre de la función es suficientemente descriptivo, no es necesario escribir un comentario detallado.

```python
# Esta función suma dos números.
def sum_numbers(a, b):
    return a + b
```

### Variables

- Usar snake_case para las variables.
```python
# Do
variable_name = 10

# Don't
variableName = 10
VariableName = 10
```

- Las constantes deben de estar en mayúsculas y separadas por guiones bajos.
```python
CONSTANT_NAME = 10
```

- Las variables deben de tener nombres descriptivos, no deben ser palabras muy abreviadas o sin sentido.
```python
# Do
number_of_students = 10
arguemnt_parser = "ArgumentParser()"

# Don't
nos = 10
num_stud = 10
ap = "ArgumentParser()"
argparse = "ArgumentParser()"
```

- Las clases deben de seguir la convención **PascalCase**, acompañadas de un comentario descriptivo.
```python
# Esta clase se encarga de la autenticación de los usuarios.
class Authentication:
    pass
```

### Archivos y Carpetas

- Los archivos y carpetas deben de tener nombres descriptivos y en minúsculas para poder ser identificados fácilmente.
```
# Do
ia_authentication.py
/get_essay_text

# Don't
ia_auth.py
/GetEssayText
```

- Los archivos de prueba debn de tener el mismo nombre que el archivo que están probando, pero con el sufijo `_test`.
```
ia_authentication.py
ia_authentication_test.py
```

## Frontend

En el frontend, escrito en JavaScript y React, seguiremos la convención **camelCase** para las variables y funciones mientras que se utilizará **PascalCase** para los archivos y carpetas. Todo código debe de estar en inglés. Los comentarios de las funciones deben incluir un comentario superior en español que explique qué hace la función y cómo lo hace, especialmente si la función es compleja.

##### Comentarios
- Los comentarios deben de estar en español, a menos que sea necesario usar un término técnico en inglés.
- Cada línea de comentario debe de tener un espacio después del símbolo `//`.
  - Para comentar varias líneas con el formato propuesto, seleccionar las líneas y presionar `Ctrl (Command) + /`.
```javascript
// Do:
// Este es un comentario.
// Con muchas líneas comentario.

// Don't:
/*
Este es un comentario.
Con muchas líneas.
*/
```
- Los comentarios con listas deben de estar indentados.
```javascript
// Do:
// Params:
//   parameterOne: Parámetro uno de la función.
//   parameterTwo: Parámetro dos de la función.

// Don't:
// Params:
// parameterOne: Parámetro uno de la función.
// parameterTwo: Parámetro dos de la función.
```
### Código JavaScript
- Las líneas de código **NO** deben terminar con punto y coma.
```javascript
// Do
const variable = 10
function sum(a, b) {
    return a + b
}

// Don't
const variable = 10;
function sum(a, b) {
    return a + b;
}
```

- Las llaves de apertura deben de estar en la misma línea que la declaración.
```javascript
// Do
function sum(a, b) {
    return a + b
}

// Don't
function sum(a, b)
{
    return a + b
}
```

- Si un `if` o un `else` solo tiene una línea de código, se pueden omitir las llaves.
```javascript

// Do
if (condition) return true
    
// Don't
if (condition) {
    return true
}
```

- Se debe utilizar **async/await** con **try/catch** en lugar de Promises.
```javascript
// Do
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data')
        const data = await response.json()
        return data
    } catch (error) {
        console.error(error)
    }
}

// Don't
function fetchData() {
    return fetch('https://api.example.com/data')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            return data;
        })
        .catch(error => {
            console.error(error);
        });
}
````

- Evita tener código muy anidado, se debe priorizar el uso de **guard clauses**.
```javascript
// Do
function authenticateUser(request) {
    if (!request || !request.user || !request.user.isAuthenticated)
        return errorResponse('User is not authenticated')
    return request.user
}

// Don't
function authenticateUser(request) {
    if (request) {
        if (request.user) {
            if (request.user.isAuthenticated) {
                return request.user
            } else {
                return errorResponse('User is not authenticated')
            }
        } else {
            return errorResponse('User is not authenticated')
        }
    } else {
        return errorResponse('User is not authenticated')
    }
}
```
### Funciones

- Usar camelCase para las funciones.
```javascript
function calculateSum(variableA, variableB) {
    return variableA + variableB
}
```

- Cada función debe de estar acompañado de un comentario que describa que hace la función, describir sus parámetros y, si es necesario, lo que regresa.
```javascript
// Esta función se encarga de enviar la rúbrica al backend.
// Params:
//   rubric: Rúbrica que se enviará al backend.
//   essayId: ID del ensayo al que se le asignará la rúbrica.
// Returns:
//   Respuesta del backend.
function sendRubric(rubric, essayId) {
    // Código de la función.
}
```

- En caso de que la función no sea muy compleja, o si el nombre de la función es suficientemente descriptivo, no es necesario escribir un comentario detallado.
```javascript
// Esta función suma dos números.
function sumNumbers(a, b) {
    return a + b
}
```

### Variables

- Usar camelCase para las variables.
```javascript
// Do
const variableName = 10

// Don't
const variable_name = 10
const VariableName = 10
```

- Se debe priorizar el uso de `const` a través del codigo. Si una variable necesita ser reasignada, se debe usar `var`.
```javascript
// Do
const array = [1, 2, 3]
array.push(4)

var number = 10
number = 20

// Don't
let array = [1, 2, 3]
array.push(4)
```

### Archivos y Carpetas
- Los archivos y carpetas deben de tener nombres descriptivos y en **PascalCase** para poder ser identificados fácilmente.
```javascript
// Do
ChatComponent.jsx
/GetEssayText
```

### Componentes React
- Los componentes de React deben de tener nombres descriptivos y en **PascalCase**.
```javascript
// Do
function EssayComponent() {
    return <div>Ensayo</div>
}

// Don't
function essay() {
    return <div>Ensayo</div>
}
```

- Los componentes de React deben de estar acompañados de un comentario que describa que hace el componente.
```javascript
// Este componente se encarga de mostrar el ensayo.
function EssayComponent() {
    return <div>Ensayo</div>
}
```

- Si al llamar a un componente no le pasamos propiedades, se debe de cerrar la etiqueta con `/>`.
```javascript
// Do
<EssayComponent />

// Don't
<EssayComponent></EssayComponent>
```

- En el caso de que un componente tenga muchas propiedades, se debe de separar cada propiedad en una línea.
```javascript
// Do
<EssayComponent
    title="Ensayo"
    author="Autor"
    date="2021-10-10"
    rubric={rubric}
    user={user}
/>

// Don't
<EssayComponent title="Ensayo" author="Autor" date="2021-10-10" rubric={rubric} user={user} />
```

- Si el componente tiene pocas propiedades, se pueden escribir en una sola línea.
```javascript
// Do
<EssayComponent essay="Ensayo" />

// Don't
<EssayComponent 
    essay="Ensayo"
/>
```