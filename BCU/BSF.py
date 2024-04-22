class Nodo:
    def __init__(self, datos, hijos=None, padre=None):
        self.datos = datos
        self.hijos = hijos
        self.padre = padre
        self.costo = None

        if self.hijos is not None:
            for h in hijos:
                h.padre = self

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos is not None:
            for h in hijos:
                h.padre = self

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
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def get_costo(self):
        return self.costo

    def _str_(self):
        return str(self.get_datos())