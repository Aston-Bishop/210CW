#CLASS Vertex:
#        FUNCTION __init__(self, id):
#             id <- id
#             neighbours <- []
#        ENDFUNCTION
#
#        FUNCTION add_neighbour(self, vert):
#            IF vert not in  neighbours:
#                 neighbours.append(vert)
#            ENDIF
#        ENDFUNCTION
#
#ENDCLASS
#
#CLASS Graph:
#        vertices <- {} 
#        FUNCTION add_vertex(self, vertex):
#            IF vertex.id not in  vertices:
#                 vertices[vertex.id] <- vertex
#            ENDIF
#        ENDFUNCTION
#
#        FUNCTION add_edge(self, start, end):
#            FOR label, vertex in  vertices.items():
#                IF label = start:
#                    start <- vertex
#                ENDIF
#                IF label = end:
#                    end <- vertex
#                ENDIF
#            ENDFOR
#            start.add_neighbour(end)
#            end.add_neighbour(start)
#        ENDFUNCTION


class Vertex:
        def __init__(self, id):
            self.id = id
            self.neighbours = []

        def add_neighbour(self, vert):
            if vert not in self.neighbours:
                self.neighbours.append(vert)

class Graph:
        vertices = {}                                                   # Using dictionary so that the vertexes can be labeled

        def add_vertex(self, vertex):
            if vertex.id not in self.vertices:
                self.vertices[vertex.id] = vertex
            else:
                print("Vertex is already in the graph")

        def add_edge(self, start, end):
            for label, vertex in self.vertices.items():
                if label == start:
                    start = vertex
                if label == end:
                    end = vertex
            start.add_neighbour(end)
            end.add_neighbour(start)

        def dfs(self, source):
            s = []
            visited = []
            s.append(source)
            while s:
                current_vert = s.pop()                                  # Removes the last element of the list
                if current_vert.id not in visited:
                    visited.append(current_vert.id)
                    for edge in current_vert.neighbours:
                        s.append(edge)

            visited_file = open('visited.txt', 'w')
            for vert in visited:
                visited_file.write("%s\n" % vert)                             

            return visited

        def bfs(self, source):
            q = []                                                      # List for a queue of vertexs edges
            visited = []
            q.append(source)

            while q:
                current_vert = q.pop(0)                                 # Removes the first element of the list
                if current_vert.id not in visited:
                    visited.append(current_vert.id)
                    for edge in current_vert.neighbours:
                        q.append(edge)

            visited_file = open('visited.txt', 'w')
            for vert in visited:
                visited_file.write("%s\n" % vert)

            return visited
        
g = Graph()

a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
g.add_vertex(Vertex('C'))
g.add_vertex(Vertex('D'))
g.add_vertex(Vertex('E'))
g.add_vertex(Vertex('F'))
g.add_vertex(Vertex('G'))
g.add_vertex(Vertex('H'))
g.add_vertex(Vertex('S'))

edges = ['AB', 'AS', 'SC', 'CD', 'CE', 'CF', 'EH', 'HG', 'SG', 'FG']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

print(g.bfs(a))
              
