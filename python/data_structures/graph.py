from data_structures.queue import Queue

class Graph:
    """
    add node
    Arguments: value
    Returns: The added node
    Add a node to the graph

    add edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    Adds a new edge between two nodes in the graph
    If specified, assign a weight to the edge
    Both nodes should already be in the Graph

    get nodes
    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)

    get neighbors
    Arguments: node
    Returns a collection of edges connected to the given node
    Include the weight of the connection in the returned collection

    size
    Arguments: none
    Returns the total number of nodes in the graph
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []

        return vertex

    def size(self):
        return len(self.adjacency_list)

    def get_nodes(self):
        return self.adjacency_list.keys()

    def add_edge(self, start_vertex, end_vertex, weight=0):
        edge = Edge(end_vertex, weight)
        if end_vertex not in self.adjacency_list:
            raise KeyError
        self.adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def breadth_first(self, vertex):
        breadth = Queue()
        nodes = []
        visited = []

        breadth.enqueue(vertex)
        visited.append(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for edge in self.get_neighbors(front):
                if edge.vertex not in visited:
                    visited.append(edge.vertex)
                    breadth.enqueue(edge.vertex)

        return nodes

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
