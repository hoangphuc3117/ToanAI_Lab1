
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

    def __init__(self, x, y, data = None):
        """
        Creates a new edge.
        :param x: source vertex
        :param y: target vertex
        :param w: optional weight
        :param data: optional data
        :param connect: whether the edge should be added to the component.
        """
        self.degree = 0 if x == y else 1
        self.v = (x,y)
        self.data = data

