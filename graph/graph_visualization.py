import networkx as nx

class GraphVisualization(object):

    def __init__(self, graph = None):
        self.graph = graph

    def loadGraph(self, graph):
        self.graph = graph

    def networkxUnGraph(self):
        edges = list(self.graph.edges())
        if self.graph is None or len(edges) == 0:
            return None
        dg = nx.Graph()
        for e in edges:
            dg.add_edge(str(e.v[0]), str(e.v[1]))
        return dg

    def networkxDiGraph(self):
        edges = list(self.graph.edges())
        if self.graph is None or len(edges) == 0:
            return None
        
        dg = nx.DiGraph()
        for e in edges:
            dg.add_edge(str(e.v[0]), str(e.v[1]))
        return dg
        