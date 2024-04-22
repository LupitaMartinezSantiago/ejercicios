from flask import Flask, render_template_string

app = Flask(__name__)

def dijkstra(grafo, nodo_inicial):
    etiquetas = {}
    visitados = []
    pendientes = [nodo_inicial]
    nodo_actual = nodo_inicial
    etiquetas[nodo_actual] = [0, '']

    while pendientes:
        nodo_actual = nodo_menor_peso(etiquetas, visitados)
        visitados.append(nodo_actual)
        pendientes.remove(nodo_actual)

        for adyacente, peso in grafo[nodo_actual].items():
            if adyacente not in visitados:
                if adyacente not in pendientes:
                    pendientes.append(adyacente)
                nuevo_peso = etiquetas[nodo_actual][0] + peso
                if adyacente not in etiquetas or etiquetas[adyacente][0] > nuevo_peso:
                    etiquetas[adyacente] = [nuevo_peso, nodo_actual]

    return etiquetas

def nodo_menor_peso(etiquetas, visitados):
    menor = float('inf')
    nodo_menor = None
    for nodo, etiqueta in etiquetas.items():
        if etiqueta[0] < menor and nodo not in visitados:
            menor = etiqueta[0]
            nodo_menor = nodo
    return nodo_menor

@app.route('/')
def index():
    grafo = {
        '1': {'3': 6, '2': 3},
        '2': {'4': 1, '1': 3, '3': 2},
        '3': {'1': 6, '2': 2, '4': 4, '5': 2},
        '4': {'2': 1, '3': 4, '5': 6},
        '5': {'3': 2, '4': 6, '6': 2, '7': 2},
        '6': {'5': 2, '7': 3},
        '7': {'5': 2, '6': 3}
    }
    etiquetas = dijkstra(grafo, '1')
    
    result = "<h1>Resultado del código Dijkstra:</h1><ul>"
    for key, value in etiquetas.items():
        result += f"<li>{key}: {value}</li>"
    result += "</ul>"
    return result

if __name__ == "__main__":
    app.run()
