""" 
    Características 
    - Estructura de datos
    - Unidimensional
    - Dinámica (No requiere un valor previo, puede adaptarse al uso)
    - Flexible
    - Eficiente en uso de memoria
    - Diseño para árboles y grafos
"""
# Clase nodo
class Nodo:
    def __init__(self, dato) -> None:
        self.dato = dato 
        self.siguiente = None

    # metodo STR
    def __str__(self) -> str:
        return str(self.dato)

# Clase lista
class Lista:
    def __init__(self) -> None:
        self.inicial = None

    # Eliminar al inicio de la lista
    def eliminarAlInicio(self):
        # Si la lista está vacía se retorna False
        if self.inicial == None:
            return False
        # Si la lista tiene datos
        self.inicial = self.inicial.siguiente
        return True

    # Inidicar si un dato esta en la lista
    def buscar(self, dato):
        # Lista vacía 
        if self.inicial == None:
            return False
        # Lista con datos
        nodo_actual = self.inicial
        while nodo_actual != None:
            if nodo_actual.dato == dato:
                return True # Encontrado
            nodo_actual = nodo_actual.siguiente
        return False # No encontrado

    # Eliminar por información (Si el dato existe)
    def eliminarPorInfo(self, dato):
    # Si la lista está vacía 
        if self.inicial == None:
            return False
        # El dato se encuentra en la cabecera
        if self.inicial.dato == dato:
            self.eliminarAlInicio()
            return True
        # Buscar dato en la lista
        nodo_previo = None
        nodo_actual = self.inicial
        while nodo_actual != None and nodo_actual.dato != dato:
            nodo_previo = nodo_actual
            nodo_actual = nodo_actual.siguiente
        # Dato no encontrado
        if nodo_actual == None:
            return False
        # Dato encontrado
        nodo_previo.siguiente = nodo_actual.siguiente
        return True
    
    # Agregar elemento al inicio de la lista
    def adicionarAlInicio(self, dato):
        # Evaluar si la lista esta vacia
        if self.inicial == None: # La lista está vacia 
            self.inicial = Nodo(dato)
        else: 
            # Si la lista tiene, al menos, un elemento
            nodo_nuevo = Nodo(dato)     # Se crea una variable para almacenar el nuevo objeto (Un nuevo nodo)
            nodo_nuevo.siguiente = self.inicial     
            self.inicial = nodo_nuevo

    # Recorrer la lista
    def __str__(self) -> str:
        recorrido = " "
        nodo_actual = self.inicial
        while nodo_actual != None: 
            recorrido += str(nodo_actual) + " -> "
            nodo_actual = nodo_actual.siguiente
        recorrido += "NULL" 
        return recorrido
    

# TALLER DE DISENO 1

    # Agregar al final de la lista
    def agregarAlFinal(self, dato):
        nodo_actual = self.inicial
        nodo_nuevo = Nodo(dato)     # Nodo nuevo
        # Evaluar si la lista esta vacia
        if self.inicial == None:
            self.inicial = nodo_nuevo
        else:
            nodo_actual = self.inicial
        # Recorrer la lista
            while nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo     # enlazar el actual al siguiente
            nodo_nuevo.siguiente = None     # Apuntar el ultimo a NULL, en este caso None

    # Indicar la cantidad de elementos de la lista
    def contarElementos(self):
        nNodos= 0       # Variable contadora donde se almacena el numero de nodos
        nodo_actual = self.inicial
        if nodo_actual == None:
            return 0
        while nodo_actual != None:
            nodo_actual = nodo_actual.siguiente
            nNodos = nNodos + 1
        return nNodos
    
    # Eliminar el ultimo elemento de la lista
    def eliminarUltimo(self):
        nodo_actual = self.inicial
        nodo_previo = None
        if nodo_actual == None:
            return False
        else:
            while nodo_actual.siguiente != None:
                nodo_previo = nodo_actual
                nodo_actual = nodo_actual.siguiente
            nodo_previo.siguiente = None
        
    # Indicar el numero de apariciones de un dato en la lista
    def contarApariciones(self, dato):
        nodo_actual = self.inicial
        nApariciones = 0
        if self.inicial == None:
            return False    # Retorna false si la lista esta vacia
        while nodo_actual != None:
            if nodo_actual.dato == dato:
                nApariciones = nApariciones + 1
            nodo_actual = nodo_actual.siguiente     # Recorrido de la lista
        return nApariciones

    def indicarElemento(self, pos):
        cont = 0
        nodo_actual = self.inicial
        # Verificar si la lista esta vacia
        if nodo_actual == None:
            return False
        # Recorrer la lista hasta la posicion deseada
        while nodo_actual != None and cont < pos:
            nodo_actual = nodo_actual.siguiente
            cont = cont + 1
        # Verificar si se alcanzo una posición valida
        if nodo_actual == None:
            return False  # Posicion fuera del rango
        else:
            return nodo_actual.dato
        
    def eliminarPosIndicada(self, pos):
        cont = 0
        nodo_actual = self.inicial
        nodo_previo = None
        if nodo_actual == None:
            return False
        while nodo_actual != None and cont < pos:
            nodo_previo = nodo_actual
            nodo_actual = nodo_actual.siguiente
            cont = cont + 1
        if nodo_actual == None:
            return False
        else:
            nodo_previo.siguiente = nodo_actual.siguiente   # "salto"
            return True 
        
    # Indicar las posiciones en las que aparece un dato en la lista
    def contarPosiciones(self, dato):
        cont = 0 
        posiciones = []
        nodo_actual = self.inicial
        if nodo_actual == None:
            return False
        while nodo_actual != None:
            if nodo_actual.dato == dato:
                posiciones.append(cont)
            nodo_actual = nodo_actual.siguiente
            cont = cont + 1
        return posiciones
            

        
                                 