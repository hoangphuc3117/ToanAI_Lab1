from .poset import Poset

class Graph(object):
    def __init__(self, vertices = None, edges = None, directed = True):
        if vertices is None:
            vertices = []
        if edges is None:
            edges = []
        self.directed = directed

        self.verticesPoset = Poset(vertices)
        self.edgesPoset = Poset([])

        for e in edges:
            x = self.verticesPoset.get(e.v[0])
            y = self.verticesPoset.get(e.v[1])
            e.v = (x, y)
            e = self.edgesPoset.add(e)
            e = self.edgesPoset.add(e)
        
    def add_edge(self, e):
        if e in self.edgesPoset:
            return self.edgesPoset.get(e)
        x = e.v[0]
        y = e.v[1]
        x = self.verticesPoset.add(x)
        y = self.verticesPoset.add(y)
        e.v = (x, y)
        e = self.edgesPoset.add(e)

    def remove_edge(self, e):
        if e not in self.edgesPoset:
            return
        self.edgesPoset.remove(e)
        return e

    def add_vertex(self, v):
        self.verticesPoset.add(v)
        return v
        
    def edges(self):
        edges = self.edgesPoset
        for e in edges:
            yield e

    def add_edges(self, edges:list):
        if edges is None:
            raise ValueError
        for e in edges:
            self.add_edge(e)
        