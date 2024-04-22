class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.costo = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos is not None:
            for h in hijos:
                h.padre = self

    def __init__(self, datos, padre=None):
        self.datos = datos
        self.padre = padre
    def get_datos(self):
        return self.datos
    def get_padre(self):
        return self.padre    
                   

    def get_hijos(self):
        return self.hijos

    def set_datos(self, datos):
        self.datos = datos

    def set_costo(self, costo):
        self.costo = costo

    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def __str__(self):
        return str(self.get_datos())