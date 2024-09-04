from listas import *

# # Creación de nodos
# nodo_01 = (1)
# nodo_02 = (3.5)
# nodo_03 = "Hola"

# # Prueba de los nodos
# print("Nodo 01: ", nodo_01)
# print("Nodo 02: ", nodo_02)
# print("Nodo 03: ", nodo_03)

# Prueba de lista
lista_01 = ListaSimple()      # Creación de la lista

lista_01.adicionarAlInicio(1)       # Adicionar elementos a lista
lista_01.adicionarAlInicio(3.5)
lista_01.adicionarAlInicio("Hola")
lista_01.adicionarAlInicio(10) 
lista_01.adicionarAlInicio(6) 
lista_01.adicionarAlInicio(7)
lista_01.adicionarAlInicio(10) 
lista_01.adicionarAlInicio(12) 
lista_01.adicionarAlInicio(7)
lista_01.adicionarAlInicio(5)

#lista_01.eliminarMultiplesApariciones(10)

penultimo = lista_01.indicarPenultimo()
print(f"El peultimo elemento de la lista es: {penultimo}")
# Prueba agregar al final de la lista
lista_01.agregarAlFinal("lol")
lista_01.eliminarUltimo()
posicion = "x"
print(f"elemento de la posicion {posicion}: {lista_01.indicarElemento(4)}")
# Prueba contar elementos de la lista
# lista_01.eliminarPosIndicada(4)
print(f"el numero {posicion}, aparece en las posiciones: {lista_01.contarPosiciones(10)}")
print(f"hay {lista_01.contarElementos()} elementos en la lista")
# Prueba contar apariciones de un elemento
print(f"el numero {10} aparece: {lista_01.contarApariciones(10)} veces")

print(f"test posiciones 2 > 5: {lista_01.elementosEntrePosiciones(2, 5)}")

print("Lista: ", lista_01)      # Imprimir la lista

lista_01.eliminarElementoAnterior(10)
print("Lista: ", lista_01)      # Imprimir la lista


# Prueba eliminar al incio
# print(lista_01.eliminarAlInicio())  # retorna true: El metodo está funcionando
# Imprimir la lista con el elemeto eliminado
# print("Lista: ", lista_01)

# Prueba eliminar por info
# print(lista_01.eliminarPorInfo("Hola"))
# print("Lista: ", lista_01)

# NOTA: Adelantar adicionar al final.