def dijkstra(Grafo, salida):
    dist, prev = {}, {}

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = set(Grafo.keys())

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)

        for vecino, peso in Grafo[u].items():
            alt = dist[u] + peso
            if alt < dist[vecino]:
                dist[vecino] = alt
                prev[vecino] = u

    return prev

def reconstruir_camino(previos, nodo):
    camino = []
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = previos[nodo]
    return camino

grafo = {
    '1': {'2': 3, '3': 6},
    '2': {'3':2, '4':1},
    '3': {'4': 4, '5': 2},
    '4': {'3': 4, '5': 6},
    '5': {'6': 2, '7':2},
    '6': {'7': 3},
    '7': {}
}

salida = '1'
nodo_destino = '7'  # Cambia este valor al nodo al que deseas llegar
previos = dijkstra(grafo, salida)
camino = reconstruir_camino(previos, nodo_destino)
print(f"Camino más corto desde el nodo {salida} hasta el nodo {nodo_destino}: {camino}")