# Redes Neuronales: 

## Trabajo Práctico: Quixo

Se desea implementar un jugador automático del juego Quixo basado en Alpha-Beta Pruning + Iterative Deepening.
Quixo es un juego de dos jugadores alternado con información perfecta y de suma cero. Quixo se juega sobre un tablero cuadrado de 5 × 5 con todas piezas iguales inicialmente en blanco. En su turno un jugador puede tomar una pieza de un borde del cuadrado que esté en blanco o que tenga su identificador. Luego debe volver a colocar la pieza, asegurándose de que ésta tenga su identificador si antes estaba en blanco, en uno de los otros bordes del tablero de forma tal que al empujar la pieza hacia adentro (y junto con ella todas las fichas en la misma fila) se vuelva a armar el tablero cuadrado.
El objetivo del juego es armar una linea de 5 piezas con el identificador propio, ya sea horizontal, vertical o diagonal. Se requiere un módulo Python con el nombre del o los alumnos presentando el TP, que incluya una clase llamada Quixo con el modelo del juego, tal que al construir una instancia modele un juego nuevo (con el tablero en blanco). La clase debe tener dos métodos, playerPlay que permite pedir la siguiente jugada a realizar y otro oponentPlay que permite registrar la jugada del oponente. 
Las jugadas deben ser modeladas con una tupla de enteros entre 1 y 20, indicando en qué posición se remueve una ficha y en qué posición se agrega (numerando las posiciones desde la esquina superior izquierda y siguiendo el sentido horario). La elección de la siguiente jugada a efectuar debe hacerse mediante el procedimiento de Alpha-Beta Pruning + Iterative Deepening. Las heurı́sticas para la valuación de una posición y el ordenamiento de las jugadas quedan a criterio de cada grupo.
En la fecha de entrega del TP se hará una competencia entre los distintos algoritmos. La competencia consta de enfrentamientos sucesivos de los distintos algoritmos desarrollados, asignando una cota de tiempo por partida a cada jugador. Es decir, si en una partida un jugador se queda sin tiempo pierde automáticamente, por lo que es importante la velocidad en la generación de la respuesta.

## Integrantes:

Ivan
Fede
Jesus

