from data_structures.graph import Graph


def direct_flights(graph, names):
    if len(names) == 0:
        return "null"

    nodes = {}
    for vertex in graph.get_nodes():
        nodes[vertex.value] = vertex

    weight = 0
    next_ = 1
    for name in names:
        if next_ < len(names):
            links = {}
            edges = graph.get_neighbors(nodes[name])
            for edge in edges:
                links[edge.vertex.value] = edge

            if names[next_] not in links.keys():
                return "null"

            weight += links[names[next_]].weight
            next_ += 1

    return weight
