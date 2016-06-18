
from collections import defaultdict

class Vertex:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.edges = {}
        self.color = 'white'
        self.predecessor = None
        self.distance = 0
        self.start_time = 0
        self.end_time = 0

    def add_neighbour(self, neighbour, weight = 0):
        self.edges[neighbour] = weight

    def adjacent(self):
        return self.edges.keys()

    def get_weight(self, neighbour):
        return self.edges[neighbour.key]

    def __str__(self):
        return str(self.key) + " " + str(self.value) + " " + self.color

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = defaultdict(list)

    def add_vertex(self, key, value):
        if key not in self.vertices:
            v = Vertex(key, value)
            self.vertices[key] = v
            return v

        raise Exception('Vertex with key already exists')

    def add_edge(self, key_from, key_to, weight = 0):
        if self.vertices[key_from] and self.vertices[key_to]:
            self.vertices[key_from].add_neighbour(self.vertices[key_to], weight)
            self.edges[key_from].append([key_to, weight])
            return

        raise Exception('Vertices with keys don\'t exist')

    def get_vertex(self, key):
        if key in self:
            return self.vertices[key]
        raise Exception('Vertex with key doesn\'t exist')

    def get_weight(self, start_vertex, end_vertex):
        neighbours = list(filter(lambda x: x[0] == end_vertex, self.edges[start_vertex]))
        if len(neighbours) > 0:
            return neighbours[0][1]
        else:
            return None


    def all_vertices(self):
        return self.vertices.keys()

    def all_edges(self):
        return self.edges.keys()

    def __contains__(self, n):
        return n in self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

def breadth_first_search(graph, start_key):

    if start_key not in graph:
        return None

    start_vertex = graph.get_vertex(start_key)

    for v in graph:
        v.color = 'white'
        v.predecessor = None
        v.distance = 0

    start_vertex.color = 'gray'

    queue = []

    queue.append(start_vertex)

    while queue:
        curr = queue.pop(0)
        for v in curr.adjacent():
            if v.color == 'white':
                v.color = 'gray'
                v.distance = curr.distance + 1
                v.predecessor = curr
                queue.append(v)
        curr.color = 'black'

def depth_first_search(graph):
    for v in graph:
        v.color = 'white'
        v.predecessor = None

    time = 0

    for v in graph:
        if v.color == 'white':
            _dfs(graph, v)

    def _dfs(graph, u):
        time += 1
        u.start_time = time
        u.color = 'gray'

        for v in u.adjacent():
            if v.color == 'white':
                v.predecessor = u
                _dfs(graph, v)

        u.color = 'black'
        time += 1
        u.end_time = time

def print_path(graph, s_key, v_key):
    s = graph.vertices[s_key]
    v = graph.vertices[v_key]

    def _print(s, v):
        if s == v:
            print(s)
        elif not v.predecessor:
            print("no path")
        else:
            _print(s, v.predecessor)
            print(v)

    _print(s,v)

if __name__ == '__main__':

    g = Graph()
    g.add_vertex('a', 1)
    g.add_vertex('b', 1)
    g.add_vertex('c', 1)
    g.add_vertex('d', 1)
    g.add_vertex('e', 1)

    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'd')
    g.add_edge('a', 'e')
    g.add_edge('e', 'd')

    breadth_first_search(g, 'a')
    print_path(g, 'a', 'd')