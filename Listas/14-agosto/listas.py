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
    
    # Eliminar por información (Si el dato existe)
    def eliminarPorInfo(self, dato):
    # Si la lista está vacía 
        if self.inicial is None:
            return False
        # El dato se encuentra en la cabecera
        if self.inicial.dato == dato:
            self.eliminarAlInicio()
            return True
        # Buscar dato en la lista
        nodo_previo = None
        nodo_actual = self.inicial
        while nodo_actual is not None and nodo_actual.dato != dato:
            nodo_previo = nodo_actual
            nodo_actual = nodo_actual.siguiente
        # Dato no encontrado
        if nodo_actual is None:
            return False
        # Dato encontrado
        nodo_previo.siguiente = nodo_actual.siguiente
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