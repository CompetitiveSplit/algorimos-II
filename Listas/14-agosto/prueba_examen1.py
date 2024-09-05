from listas import *

def test_elementosExclusivos():
    l1 = ListaDoble()
    l2 = ListaDoble()
    l1.adicionarAlInicio(4)
    l1.adicionarAlInicio(2)
    l1.adicionarAlInicio(3)
    l1.adicionarAlInicio(5)
    l1.adicionarAlInicio(6)
    l2.adicionarAlInicio(2)
    l2.adicionarAlInicio(4)
    l2.adicionarAlInicio(5)
    l2.adicionarAlInicio(7)
    l2.adicionarAlInicio(4)

    # Lista vacia
    l4 = ListaDoble()

    # l1 = 6 <-> 5 <-> 3 <-> 2 <-> 4
    # l2 = 4 <-> 7 <-> 5 <-> 4 <-> 2

    l3 = ListaDoble().elementosExclusivos(l1, l2)

    print("Lista merge: ", l3)

test_elementosExclusivos()