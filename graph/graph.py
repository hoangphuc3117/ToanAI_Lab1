from .poset import Poset
from collections import deque # to optimize the time when using BFS

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
        e.attach()
        e = self.edgesPoset.add(e)

    def remove_edge(self, e):
        if e not in self.edgesPoset:
            return
        e.detach()
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

    def vertices(self):
        for v in self.verticesPoset:
            yield v
    
    def get_vertex_from_data(self, data):
        if data is None:
            return None
        for v in self.vertices():
            if v.data is not None and str(v.data) == str(data):
                return v
        return None
        
    
    def find_child_path(self, start_vertex):
        queue = deque()
        queue.append([start_vertex]) 
        child_paths = set() 
        visited = set()
        while queue:
            path = queue.popleft()
            vertex = path[-1]
            child_paths.add(tuple(path)) 
            if vertex in visited:
                continue 
            visited.add(vertex)
            for e in vertex.e_in():
                child = e.v[1]
                new_path = list(path) 
                new_path.append(child) 
                queue.append(new_path)
        return list(child_paths)
    
    def is_directed(self):
        return self.directed
    
    def BFS(self, start_vertex): 
        queue = deque()
        queue.append(start_vertex)
        visited = set() 
        child_paths = set()
        while queue:
            vertex = queue.popleft() 
            if vertex in visited:
                continue 
            visited.add(vertex) 
            child_paths.add(vertex)
            for e in vertex.e_dir(0):
                if e.v[0] == vertex:
                    child = e.v[1]
                else:
                    child = e.v[0]
                queue.append(child)
        return child_paths