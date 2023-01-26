import networkx as nx

class GraphVisualization(object):

    def __init__(self, graph = None):
        self.graph = graph

    def loadGraph(self, graph):
        self.graph = graph

    def networkx(self):
        edges = list(self.graph.edges())
        if self.graph is None or len(edges) == 0:
            return None
        if self.graph.is_directed():
            dg = nx.Graph()
        else:
            dg = nx.DiGraph()
        for e in edges:
            dg.add_edge(str(e.v[0]), str(e.v[1]))
        return dg
        
        