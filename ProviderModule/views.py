from flask import request
from flask_cors import CORS, cross_origin
from ProviderModule import app
import networkx as nx
import json

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/healthping')
@cross_origin()
def healthPing():
    return ("I am alive!", 200)

@app.route('/processGraph', methods=["POST"])
@cross_origin()
def processGraph():
    data = json.loads(request.data.decode('utf-8'))
    nodes = data['nodes']
    edges = [(x[0], x[1]) for x in data['edges']]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    positions = nx.kamada_kawai_layout(graph)
    positions = {key: list(map(lambda x: round(x, 2), list(value))) for key, value in positions.items()}
    res = json.dumps(positions)
    return (res, 200)
