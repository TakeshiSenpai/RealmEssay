## Preguntas frecuentes sobre vercel
## Precios
#### ¿Cuál es el costo?

Los costos los toma según el uso de la cuenta, no de un solo servidor, estos se maneja por cuanto tiempo se utiliza de la solicitudes de borde a la cpu, velocidad de transferencia y ancho de banda, realmente utiliza muchos parametros, [aqui](https://vercel.com/docs/pricing) hay un poco mas de información.
#### ¿El proyecto es sostenible sin necesidad de pagar?

Respuesta corta si. Observando un poco el comportamiento del uso que le di para ser posible que pueda existir esta página web sin necesidad de pagar, claro tomando en cuenta que nuestra trafico siempre se mantenga bajo, ademas de que inevitablemente llegará a un punto que se pasará lo limites de prueba y se deberá pagar
## Uso
#### ¿Cuál es la raíz?

Según que servidor se este usando se cambia la raíz a la hora de subir el proyecto, esto puede ser un problema cuando se trata de invocar funciones fuera de esta, aunque solo se debe tener en cuenta que la raíz cambio.

#### ¿Se le puede dar un URL personalizado?
Si, pero se debe pagar, o mas bien ser dueño de la dirección que pues en escencia en lo mismo, asi que nos quedaremos con la extensión vercel.app (o cualquier cosa rara que nos ponga vercel) para todo nuestros proyectos.

#### ¿Cómo se sube el proyecto?
Para subirlo se debe sincronizar con el repositorio, y puedes elegir si hacer deployment o no. Vercel hace unas pruebas para revisar que este todo en orden y que se pueda subir.

#### ¿Cual es el maximo de deployments que se puede?

Se puede un total de 100 deployments cada 24 horas, en el caso de como lo tenemos estructurado, cada vez que se haga un commit puede que se haga un hasta cinco deployments ya que todos nuestros servidores estan en mismo repositorio, por lo tanto 100/5 son un total de 25 deployments al dia.

#### ¿Se puede trabajar como equipo o alguien debe tener el total control?

En vercel existe una función para trabajar con un equipo falta probarla como equipo para observar la funcionalidad

#### ¿Qué rama utiliza vercel para hacer un deployment?

La rama que utiliza es la que es por default, en nuestro caso el main, pero podriamos cambiar a otra rama.

#### ¿Teniendo Vercel ya no lo usaremos en local?

Yo opino que mantengamos las dos versiones una en vercel y otra en local, por el tema de la cantidad de deployments que se puede hacer, usualmente cuando estas probando cosas haces muchos cambios al código y por ende muchos deployments y será frustante sí se acaban los deployments del dia.

#### ¿Porqué ahora tenemos muchos requeriments?

Porque cada servidor tiene su propio python, entonces me parecio correcto que cada servidor descargara solo las librerias correspondientes.

#### ¿Es necesario que se llamen index.py todos los archivos?

De momento si, no encontre una forma que me permitiera cambiar el nombre, de seguro en el vercel.json debe ser posible pero en mi opinión no supone ningun problema.

#### ¿Toca cambiar los fetch en el frontend?

No, se usa variables de entorno para que sea compatible el uso de vercel tanto en local con un autorun
## Conclusión

Vercel esta muy bueno y pienso que nuestro proyecto no debería migrarse por completo a la nube sino mantener los dos formatos, ademas nunca deberíamos pagar en vercel porque realmente es caro, pero es posible crear una nueva cuenta cuando se acabe el limite gratuito 😈