from flask import Flask, jsonify
from BSF import Nodo

app = Flask(__name__)

def DFS_prof_iter(nodo, solucion, conexiones):
    for limite in range(0, 100):
        visitados = []
        sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite, conexiones)
        if sol is not None:
            return sol

def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite, conexiones):
    if limite >= 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            # Expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)

            nodo.set_hijos(lista_hijos)

            for nodo_hijo in nodo.get_hijos():
                if nodo_hijo.get_datos() not in visitados:
                    # Llamada recursiva
                    sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite-1, conexiones)
                    if sol is not None:
                        return sol
        return None

@app.route('/')
def encontrar_ruta():
    conexiones = {
        'EDO.MÉX': {'QRO', 'SLP', 'SONORA'},
        'PUEBLA': {'HIDALGO', 'SLP'},
        'CDMX': {'MICHOACAN'},
        'MICHOACAN': {'SONORA'},
        'SLP': {'QRO', 'PUEBLA', 'EDO.MÉX', 'SONORA', 'GUADALAJARA'},
        'QRO': {'EDO.MÉX', 'SLP'},
        'HIDALGO': {'PUEBLA', 'GUADALAJARA', 'SONORA'},
        'MONTERREY': {'HIDALGO', 'SLP'},
        'SONORA': {'MONTERREY', 'HIDALGO', 'SLP', 'EDO.MÉX', 'MICHOACAN'},
        'GUADALAJARA': {'SLP', 'HIDALGO'}
    }

    estado_inicial = 'EDO.MÉX'
    solucion = 'HIDALGO'
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion, conexiones)

    if nodo is not None:
        resultado = []
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        return jsonify(resultado)
    else:
        return jsonify({"error": "Solución no encontrada"})

if __name__ == "__main__":
    app.run(debug=True)
