import functools
from .BSF import Nodo

def compara(x, y):
    return x.get_costo() - y.get_costo()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    nodos_frontera.append(nodo_inicial)
    
    while not solucionado and len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, key=functools.cmp_to_key(compara))
        nodo = nodos_frontera[0]
        nodos_visitados.append(nodos_frontera.pop(0))
        
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            
            for un_hijo in conexiones[dato_nodo]:                
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_costo(nodo.get_costo() + coste)
                lista_hijos.append(hijo)
                
                if not hijo.en_lista(nodos_visitados):
                    if hijo.en_lista(nodos_frontera):               
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                
                nodo.set_hijos(lista_hijos)
                            
conexiones = {
    'EDO.MEX': {'SLP': 513, 'CDMX': 125},
    'PUEBLA': {'SLP': 514},
    'CDMX': {'MICHOACAN': 491, 'SLP': 423, 'EDO.MEX': 125},
    'MICHOACAN': {'SONORA': 346, 'SLP': 355, 'MONTERREY': 309, 'CDMX': 491},
    'SLP': {'QRO': 203, 'PUEBLA': 514, 'EDO.MEX': 513, 'SONORA': 603, 'GUADALAJARA': 437, 'CDMX': 423,
            'MICHOACAN': 355, 'MONTERREY': 313, 'HIDALGO': 599},
    'QRO': {'SLP': 203, 'HIDALGO': 390},
    'HIDALGO': {'QRO': 390, 'SLP': 599},
    'MONTERREY': {'SLP': 313, 'SONORA': 296, 'GUADALAJARA': 394, 'MICHOACAN': 309},
    'SONORA': {'MONTERREY': 296, 'SLP': 603, 'MICHOACAN': 346},
    'GUADALAJARA': {'MONTERREY': 394, 'SLP': 437}
}
estado_inicial = 'EDO.MEX'
solucion = 'HIDALGO'
nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)

resultado = []
nodo = nodo_solucion

while nodo.get_padre() is not None:
    resultado.append(nodo.get_datos())
    nodo = nodo.get_padre()

resultado.append(estado_inicial)
resultado.reverse()

print(resultado)
print('Costo: ' + str(nodo_solucion.get_costo()) + ' KM')