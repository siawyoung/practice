
# Dijkstra

import graph

g = graph.Graph()
g.add_vertex('a', 1)
g.add_vertex('b', 1)
g.add_vertex('c', 1)
g.add_vertex('d', 1)
g.add_vertex('e', 1)

g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 5)
g.add_edge('c', 'd', 2)
g.add_edge('a', 'e', 1)
g.add_edge('e', 'd', 4)

def dijkstra(graph, start_vertex):
    distances = {}
    vertices_already_considered = set()

    # we recompute the closest vertex every time, but we can also use a priority queue
    # this is the dominating computation in dijkstra

    # currently, this causes dijkstra to take O(v^2) time, because everytime we want to find the next
    # closest vertex, we are checking through all the vertices

    # Dijkstra can be improved to O((E + V)logV) by using a heap instead
    def closest_vertex():
        _min = float('inf')
        closest_vertex = None
        for v in graph.all_vertices():
            if v not in vertices_already_considered and distances[v] <= _min:
                _min = distances[v]
                closest_vertex = v
        return closest_vertex

    # initialize all the distances as infinity
    for v in graph.all_vertices():
        distances[v] = float('inf')

    # the distance to the starting vertex from itself is of course 0
    distances[start_vertex] = 0

    for i in range(len(graph.all_vertices()) - 1):
        closest = closest_vertex()
        vertices_already_considered.add(closest)

        # we update the distances for all the unadded vertices
        # to be eligible for updating, we check if
        # 1) the vertex is not already considered
        # 2) there is an edge from the closest edge to the vertex being considered
        # 3) the distance from the source vertex to the closest vertex is not infinity
        # 4) that the distance to the closest vertex from the source vertex PLUS the weight of the edge from the closest vertex is less than the current closest known distance to that vertex

        for other_vertex in graph.all_vertices():

            if (other_vertex not in vertices_already_considered and
                graph.get_weight(closest, other_vertex) and
                distances[closest] != float('inf') and
                distances[closest] + graph.get_weight(closest, other_vertex) < distances[other_vertex]
               ):

                distances[other_vertex] = distances[closest] + graph.get_weight(closest, other_vertex)


    return distances

print(dijkstra(g, 'a'))
