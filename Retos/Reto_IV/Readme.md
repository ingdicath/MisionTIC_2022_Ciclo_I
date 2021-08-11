# Reto 4: Grupo P1

## ArpaLlanera Hero: "Fail in the Note"

Luego del gran éxito de ArpaLLanera Hero, Deiv Mostacho decide continuar con esta gran idea, pero enfocado hacia otros jugadores, así que se le ocurre construir una app para tener una versión del juego para dispositivos móviles pero con una dinámica diferente, por cuestiones de derechos de autor y de seguir sus propias ideas.

Deiv estaba mirando programas viejos colombianos, y se encuentra con uno que tenía un concurso llamado "Caiga en la Nota", el cual le pareció muy interesante y le sirvió de inspiración. Se le ocurrió un juego como el que se describe a continuación: un usuario va a escucha la canción, y va a ir escribiendo las cuerdas (separadas por guión) que considera están sonando, en donde cada cuerda sólo va a sonar una única vez. El juego tendrá un conjunto con las notas válidas en la canción, y si la nota escrita por el jugador está en el conjunto de notas válidas, recibirá una puntuación que está almacenada también en el conjunto.

Así, el jugador recibirá al final el puntaje que obtuvo (de acuerdo a las cuerdas a las que le atino) y el listado de cuerdas válidas en el orden que las escribió y separadas por coma.

A continuación se muestra un ejemplo para hacer esto más claro:

Conjunto de cuerdas válidas = ```{"i": 90, "n": 25, "t": 32, "l": 24, "j": 23, "r": 54, "h": 34, "z": 36, "p": 95, "k": 86, "e": 67, "g": 27, "u": 54, "x": 57, "m": 94}```

Cuerdas escritas por el jugador: ```r-p-q-g-h-k-l-x-b-s-o-e-y-m-z```

Entonces el puntaje sería **574**, debido a que las notas válidas a las que atino el jugador son: ```r,p,g,h,k,l,x,e,m,z```; así que el puntaje se calcula: _54+95+27+34+86+24+57+67+94+36=574_.

Usted se cansó de ser el jalacables de los otros melenudos raros, así que se contacta con Deiv para desarrollar el video juego en versión de móvil. Así, usted va a desarrollar un programa que reciba el conjunto de cuerdas válidas junto con el puntaje que otorgan, y las cuerdas escritas por el jugador seperadas por un guión. Calculará el puntaje, y se lo mostrará al usuario, junto con las cuerdas correctas de las escritas por el jugador, y separadas por coma.

<br >**Entrada**

En la primera línea, va a recibir una cadena de caracteres, que contendrá un diccionario cuyas claves serán cadenas de caracteres y sus valores serán números enteros. En la segunda línea, va a recibir una cadena de caracteres que corresponde a las cuerdas escritas por el jugador, y separadas por guión.

**Salida**

En la primera línea se debe escribir el puntaje obtenido por el jugador. En la segunda línea, se debe escribir una cadena de caracteres con las cuerdas válidas que atino el jugador, en el mismo orden que las escribió el jugador, y separadas por coma.

|  Entrada  | Salida    |
| --------  |-----------|
| {"i": 90, "n": 25, "t": 32, "l": 24, "j": 23, "r": 54, "h": 34, "z": 36, "p": 95, "k": 86, "e": 67, "g": 27, "u": 54, "x": 57, "m": 94}| 574                   |
| r-p-q-g-h-k-l-x-b-s-o-e-y-m-z | r,p,g,h,k,l,x,e,m,z   |

