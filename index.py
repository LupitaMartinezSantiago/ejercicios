from flask import Flask, render_template, request, jsonify
from BCU.BCU import buscar_solucion_UCS as BCU_buscar_solucion
from BCU.BCU import conexiones

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_BCU', methods=['POST'])
def buscar_BCU():
    estado_inicial = request.form['estado_inicial']
    solucion = request.form['solucion']
    nodo_solucion = BCU_buscar_solucion(conexiones, estado_inicial, solucion)
    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    costo_BCU = nodo_solucion.get_costo()

    return jsonify({'resultado_BCU': resultado, 'costo_BCU': costo_BCU})

@app.route('/buscar_dijkstra', methods=['POST'])
# Aquí puedes implementar la lógica para buscar con Dijkstra
def buscar_dijkstra():
    
 
    resultado_dijkstra = "Camino más corto : ['1', '2', '3', '5', '7']"
    # Por ahora, solo devuelve un resultado de ejemplo
    return render_template('index.html', resultado_dijkstra=resultado_dijkstra)

if __name__ == '__main__':
    app.run(debug=True)


