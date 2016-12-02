class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbours = {}
        self.dist = None
        self.prev = None

    def add_neighbour(self, vert, weight):
        if vert not in self.neighbours:
            self.neighbours[vert] = weight

class Graph:
    vertices = {} # Using dictionary so that the vertexes can be labeled

    def add_vertex(self, vertex):
        if vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
        else:
            print("Vertex is already in the graph")

    def add_edge(self, u, v, weight):
        for label, vertex in self.vertices.items():
            if label == u:
                u = vertex
            if label == v:
                v = vertex
        u.add_neighbour(v, weight)
        v.add_neighbour(u, weight)

    def Dijkstra(self, start, dest):
        unvisited = []
        for vertex in g.vertices:
            g.vertices[vertex].dist = float('inf')                  #setting distance from start for each node to infinite
            unvisited.append(g.vertices[vertex])

        start.dist = 0

        while unvisited:
            min_dist = None
            for vertex in unvisited:
                if min_dist == None:
                    min_dist = vertex
                elif vertex.dist < min_dist.dist:
                    min_dist = vertex
            unvisited.remove(min_dist)
            current = min_dist
            
            for edge in current.neighbours:
                alternate_dist = current.dist + edge.neighbours[current]
                if alternate_dist < edge.dist:
                    edge.dist = alternate_dist
                    edge.prev = current

            if current == dest:
                path = []
                while current:
                    path.insert(0, current.id)
                    current = current.prev

        return(path)
        
g = Graph()

a = Vertex('A')
g.add_vertex(a)
b = Vertex('B')
g.add_vertex(b)
g.add_vertex(Vertex('C'))
g.add_vertex(Vertex('D'))
e = Vertex('E')
g.add_vertex(e)
s = Vertex('S')
g.add_vertex(s)


edges = ['SA1', 'SC2', 'CA4', 'AB6', 'CD3', 'BD1', 'DE1', 'BE2']
for edge in edges:
    g.add_edge(edge[:1], edge[1:2], int(edge[2:]))

print(g.Dijkstra(s,e))
