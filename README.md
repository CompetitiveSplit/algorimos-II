# algorimos-II
Algoritmos II, Universidad de la Costa 2024-2

Clase 21 de agosto: se hicieron modificaciones a _listas.py_: 
* Se añadió el metodo _eliminarAlInicio_ para eliminar el primer objeto en la lista
    El método mueve la cabecera al nodo siguiente. El nodo que tenía la cabecera se pierde.
* Se añadió el método _eliminarPorInfo_ para eliminar basado en la info del nodo:
    El método recorre la lista buscando el dato dato y cuando lo encuentra da un salto del nodo previo al nodo siguiente de donde esta el dato.
    ej: 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
    si se va a borrar el dato 4, se hace un salto del nodo 3 al 5.


TODO:
* Revisar la implementacion del ultimo punto del taller.