# Reto 5: Grupo P1

## Los Jinetes del Arpacalipsis

Deiv Mostacho ha hecho las pases con James Hammett, Kirk Hetfield, Cliff Newsted y Lars Trujillo, y han decidido unificar todos los videojuegos de ArpaLlanera Hero que han desarrollado. Para ello, quieren hacer un concierto que han denominado "Los Jinetes del Arpacalipsis", y para ello han llamado más melenudos a cantar con ellos, y han decidido armar la lista de invitados. Deiv y James han hecho las listas de invitados en nombre de sus compañeros, pero cada uno por aparte, lo cual como es de esperar tendrá problemas, por un lado porque tienen algunos conocidos en común, y por otro lado, porque ponerlos de acuerdo no suele ser sencillo.

Usted los está escuchando discutir, y se da cuenta que desde ya puede adivinar algunos de los problemas que van a pasar, y que fijo lo van a poner a programar una solución para eso; anticipándose, decide crear un módulo de Python propio para que cuando sea el momento, usted invoque soluciones que ya ha definido, y con eso, además de resolverles el problema, no se aguanta la intensidad de los melenudos esos. Ya llegaron los invitados, y están formados en una fila, por el mismo desorden de información a cada uno se le asigno un turno en orden de llegara (la primera persona que llega tiene el primer turno). Usted ha decidido llamar a la librería 'arpacalipsis' [1 punto], y le va a colocar las siguientes funciones:

1) Función **tipo_melenudos** que va a recibir una lista, la cual se obtiene de una columna de la lista de invitados que determina el tipo de melenudo. Para facilitar el ingreso, se deben determinar los tipos de melenudos existentes, así que la función debe retornar los tipos de melenudos sin repetir que aparecen en dicha lista.

Por ejemplo. si la lista original es:

```tipo_melenudos(['jalacables', ´poguero', 'jalacables', 'showsero', 'poguero', 'poguero'])```

La función debería retornar:

```['jalacables', 'poguero', 'showsero']```


2) Función **si_son**, la cual va a recibir algunos turnos de la fila, una lista con el tipo de melenudo de cada uno de los melenudos en la fila (en el mismo orden de llegada, es decir, el primer tipo de la lista corresponde al primer melenudo en la fila), y un tipo de melenudo a verificar en los turnos definidos, esto porque entre tanta gente, se confunde un poco el invitado a qué área se debe dirigir, y también es complicado confiar del todo en la palabra de cada uno: todos quieren ver el show de la forma más relajado posible. Así que la función va a retornar una lista con los turnos de los ingresados que efectivamente tienen el tipo de melenudo que se está verificando.

Por ejemplo, si los parámetros son:

`si_son([1,3,5,7], ['jalacables', ´poguero', 'jalacables', 'showsero', 'poguero', 'poguero', 'showsero', 'jalacables'], 'jalacables')`

La función debería retornar:

`[7]`


3) La función **no_estan**, la cual va a recibir dos listas: los turnos en la fila de los invitados en la lista de Deiv, y los turnos en la fila de los invitados por James, y debe determinar cuales de los invitados de Deiv no han sido invitados por James (para evitar confusiones, y también evitar colados). 

Por ejemplo, a la siguiente entrada:

`no_estan([1,2,3,5,7,8], [2,3,7,8])`

La salida debería ser:

`[1,5]`


4) La función **uno_y_uno**, que va a recibir la lista de Deiv y la lista de James. Esta función surge por un motivo, se está llenando el lugar del evento, y James ha discutido con Deiv de quién debería entrar. Han logrado llegar al acuerdo de que de los invitados que no están en ambas listas, va a entrar uno y uno de cada lista. La función debe retornar la cantidad de personas de cada lista que podrían entrar al evento.

Por ejemplo, a la siguiente entrada:

`uno_y_uno([1,2,4,5,7,8], [2,3,7,8])`

La salida debería ser:

`1`

porque de la lista de James (segunda lista) solo el turno 3 es válido para ingresar, y así un invitado de la lista de Deiv, en este caso el del turno 1, podría ingresar como corresponde.

<br >**Entrada**:

Este programa no requiere entrada. Ni generará salida. Se requiere que el estudiante genere un archivo con el nombre **arpacalipsis.py** y que se respeten los nombres de las funciones dadas y sus parámetros.

