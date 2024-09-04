# Clase Nodo Simple
class NodoSimple:
    # Constructor
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    # Str
    def __str__(self) -> str:
        return str(self.dato)
    
    # Eq
    def __eq__(self, other):
        if not isinstance(other, NodoSimple):
            return False
        return self.dato == other.dato

# Clase ListaSimple
class ListaSimple:
    # Constructor
    def __init__(self) -> None:
        self.nodoInicial = None

    # Lista Vacia
    def estaVacia(self):
        return self.nodoInicial == None

    # Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo

    # Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato

    # Buscar por dato
    def buscar(self, dato_buscar):
        if self.estaVacia():
            return False
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    return True
                nodoActual = nodoActual.siguiente
            return False

    # Str
    def __str__(self):
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual.dato) + " -> "
            nodoActual = nodoActual.siguiente
        recorrido += "NULL"
        return recorrido

    # Eliminar por información
    def eliminarInfo(self, dato_eliminar):
        if self.estaVacia():
            return False
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return False
        nodoPrevio.siguiente = nodoActual.siguiente
        return True

    # Agregar al final de la lista
    def agregarAlFinal(self, dato):
        nodoNuevo = NodoSimple(dato)  # Nodo nuevo
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nodoNuevo  # Enlazar el actual al siguiente

    # Indicar la cantidad de elementos de la lista
    def contarElementos(self):
        nNodos = 0  # Variable contadora donde se almacena el número de nodos
        nodoActual = self.nodoInicial
        while nodoActual != None:
            nodoActual = nodoActual.siguiente
            nNodos += 1
        return nNodos

    # Eliminar el último elemento de la lista
    def eliminarUltimo(self):
        if self.estaVacia():
            return False
        nodoActual = self.nodoInicial
        nodoPrevio = None
        while nodoActual.siguiente != None:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        if nodoPrevio is not None:
            nodoPrevio.siguiente = None
        else:
            self.nodoInicial = None
        return True

    # Indicar el número de apariciones de un dato en la lista
    def contarApariciones(self, dato):
        nodoActual = self.nodoInicial
        nApariciones = 0
        if self.estaVacia():
            return 0  # Retorna 0 si la lista está vacía
        while nodoActual != None:
            if nodoActual.dato == dato:
                nApariciones += 1
            nodoActual = nodoActual.siguiente  # Recorrido de la lista
        return nApariciones

    # Indicar el elemento en una posición indicada de la lista, si existe.
    def indicarElemento(self, pos):
        cont = 0
        nodoActual = self.nodoInicial
        # Verificar si la lista está vacía
        if self.estaVacia():
            return None
        # Recorrer la lista hasta la posición deseada
        while nodoActual != None and cont < pos:
            nodoActual = nodoActual.siguiente
            cont += 1
        # Verificar si se alcanzó una posición válida
        if nodoActual == None:
            return None  # Posición fuera del rango
        else:
            return nodoActual.dato

    # Eliminar una posición indicada de la lista, si existe.
    def eliminarPosIndicada(self, pos):
        cont = 0
        nodoActual = self.nodoInicial
        nodoPrevio = None
        if self.estaVacia():
            return False
        while nodoActual != None and cont < pos:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
            cont += 1
        if nodoActual == None:
            return False
        else:
            if nodoPrevio is None:  # Si estamos eliminando el primer nodo
                self.nodoInicial = nodoActual.siguiente
            else:
                nodoPrevio.siguiente = nodoActual.siguiente   # "salto"
            return True

    # Indicar las posiciones en las que aparece un dato en la lista
    def contarPosiciones(self, dato):
        cont = 0
        posiciones = []
        nodoActual = self.nodoInicial
        if self.estaVacia():
            return posiciones
        while nodoActual != None:
            if nodoActual.dato == dato:
                posiciones.append(cont)
            nodoActual = nodoActual.siguiente
            cont += 1
        return posiciones
    
    # Indicar el penultimo dato de la lista
    def indicarPenultimo(self):
        nodoActual = self.nodoInicial
        nodoPrevio = None
        if self.estaVacia():
            return False
        else:
            while nodoActual.siguiente != None:
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
            return nodoPrevio.dato
        
    # Inidicar elementos entre dos posiciones SI posicion_inicial > posicion
    def elementosEntrePosiciones(self, inicial, final):
        nodoActual = self.nodoInicial
        contador_inicio = 0
        valores = []
        if self.estaVacia():
            return False
        if inicial > final:
            return False
        # Avanzar hasta la pos inicial
        while nodoActual is not None and contador_inicio < inicial:
            nodoActual = nodoActual.siguiente
            contador_inicio += 1
        # Verificar pos inicial
        if nodoActual is None:
            return False
        while nodoActual is not None and contador_inicio < final - 1:
            nodoActual = nodoActual.siguiente
            valores.append(nodoActual.dato)
            contador_inicio += 1
        return valores      # Retorno de los numeros entre posiciones
    
    # Eliminar todas las apariciones de un dato en la lista
    def eliminarMultiplesApariciones(self, dato_eliminar):
        if self.estaVacia():
            return False
    # Cuando el dato a eliminar está en el nodo inicial
        while self.nodoInicial != None and self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
    # sino:
        nodoActual = self.nodoInicial
        nodoPrevio = None
        while nodoActual != None:
            if nodoActual.dato == dato_eliminar:
                if nodoPrevio != None:
                    nodoPrevio.siguiente = nodoActual.siguiente
                # Mover el nodoActual al siguiente
                nodoActual = nodoActual.siguiente
            else:
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
        return True
    
    # Eliminar el elemento anterior del indicado por el usuario
    def eliminarElementoAnterior(self, dato):
        if self.estaVacia():
            return False
        nodoActual = self.nodoInicial
        nodoPrevio = None
        while nodoActual != None and nodoActual.siguiente != None:
            if nodoActual.siguiente.dato == dato:
                if nodoPrevio == None:
                    # Cuando el nodo a eliminar es el nodo inicial
                    self.eliminarAlInicio()
                else:
                    nodoPrevio.siguiente = nodoActual.siguiente
                # Avanzar al siguiente nodo
                nodoActual = nodoActual.siguiente
            else:
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente    
        return True
    
class NodoDoble(NodoSimple):
    # Constuctor
    def __init__(self, dato):
        super().__init__(self, dato)
        super.__init__(dato)
        self.previo = None

    def __eq__(self, other):
        if not isinstance(other, NodoDoble):
            return False 
        return self.dato == other.dato

# Clase ListaDoble
class ListaDoble(ListaSimple):
    # Constructor
    def __init__(self) -> None:
        super().__init__()

    # Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial.previo = nodoNuevo
            self.nodoInicial = nodoNuevo

    #Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            if self.nodoInicial != None:
                self.nodoInicial.previo = None
            return dato

    # Eliminar por información
    def eliminarInfo(self, dato_eliminar):
        if self.estaVacia():
            return False
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return False
        nodoPrevio = nodoActual.previo
        if nodoActual.siguiente == None:
            nodoPrevio.siguiente = None
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
            nodoSiguiente = nodoActual.siguiente
            nodoSiguiente.previo = nodoPrevio

