from flask import request
from flask_cors import CORS, cross_origin
from ProviderModule import app
import networkx as nx

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
    edges = data['edges']
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    positions = nx.spring_layout(graph)
    res = json.dumps(positions)
    return (res, 200)
