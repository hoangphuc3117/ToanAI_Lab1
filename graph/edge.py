
class Edge(object):
    """

    Base class for edges.

    **Attributes**
          - degree (int): degree of the edge (number of unique vertices).
          - v (list[Vertex]): list of vertices associated with this edge.
    """
    degree: int
    """Is 0 if a loop, otherwise 1."""

    data: object

    def __init__(self, x, y, w = 0, data = None):
        """
        Creates a new edge.
        :param x: source vertex
        :param y: target vertex
        :param w: optional weight
        :param data: optional data
        """
        self.degree = 0 if x == y else 1
        self.v = (x,y)
        self.data = data
    
    def __lt__(self, v):
        return 0

    def __gt__(self, v):
        return 0

    def __le__(self, v):
        return 0

    def __ge__(self, v):
        return 0

    def attach(self):
        """
            Attach this edge to the edge collections of the vertices.
        """
        if self not in self.v[0].e:
            self.v[0].e.append(self)
        if self not in self.v[1].e:
            self.v[1].e.append(self)

    def detach(self):
        """
            Removes this edge from the edge collections of the vertices.
        """
        if self.degree == 1:
            assert self in self.v[0].e
            assert self in self.v[1].e
            self.v[0].e.remove(self)
            self.v[1].e.remove(self)
        else:
            if self in self.v[0].e:
                self.v[0].e.remove(self)
            assert self not in self.v[0].e
        return [self]
    
    def __getstate__(self):
        xi, yi = (self.v[0].index, self.v[1].index)
        return (xi, yi, self.w, self.data)

    def __setstate__(self, state):
        xi, yi, self.w, self.data
        self._v = [xi, yi]
        self.degree = 0 if xi == yi else 1

    def __str__(self):
        return f"""{self.v[0].data}->{self.v[1].data}"""
    
    def __repr__(self):
        return f"""{self.v[0].data}->{self.v[1].data}"""