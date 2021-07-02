# Reto 2: Grupo P1

## ArpaLLanera Hero

James Hammett y Kirk Hetfield están viajando hacia Colombia, y quieren conocer más de su cultura. Así que deciden crear un videojuego para estudiar música tradicional colombiana un poco más, y se encuentran con una gran idea: ArpaLlanera Hero. Este es un videojuego en donde se tienen 26 cuerdas (mencionadas de la A a la Z), y ellos deben adivinar correctamente la cuerda que suena para acumular puntos y así definir al ganador.

La dinámica del juego es la siguiente: cada uno de los jugadores va a seleccionar un grupo de cuerdas, donde el grupo de ambos debe ser de la misma cantidad de cuerdas, e incluso los jugadores pueden escoger la misma cuerda como parte de sus grupos. Si la cuerda que suena está en el grupo de alguno de los jugadores se le asigna un punto a dicho jugador, y luego se comparan las puntuaciones de cada uno; si James lleva más puntos se anota una 'J', si Kirk lleva más puntos se anota una 'K', y si llevan los mismos puntos se anota una 'L'.

Curiosamente, usted está en el mismo bus como "jalacables", pero ellos recuerdan que usted sabe programación, y le solicitan crear un programa que reciba el grupo letras que corresponden al grupo de cuerdas con las que juega de James (como una cadena de caracteres), luego reciba el grupo de cuerdas con las que juega Kirk (como una cadena de caracteres), y finalmente el conjunto de cuerdas que van a sonar en el juego de manera secuencial (también como una cadena de caracteres). El programa debe mostrar en la consola las anotaciones realizadas en la dinámica del juego.

<br >**Entrada**

La entrada consta de tres cadenas de caracteres separadas por fin de línea. La primera línea corresponde al grupo de cuerdas de James, la segunda línea corresponde al grupo de cuerdas de Kirk, y una tercera que corresponde a la secuencia de cuerdas que sonarán en el juego.

**Salida**

Una cadena de caracteres con las letras J, K y L, dependiendo de las puntuaciones que vaya teniendo cada jugador cada vez que suena una cuerda.

| 			Entrada         |              Salida                      |
| --------------------------|------------------------------------------|
| AHS                       | LLLLKKKKKKKKKKKKKKKKKKKK                 |
| SDA                       |                                          |
| AJSSDSAASASASSASADAJAJSS  |                                          |