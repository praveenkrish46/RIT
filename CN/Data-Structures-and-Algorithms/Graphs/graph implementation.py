class Graph:
    def __init__(self):
        self.graph = {}                              

    def addVertex(self, vertex):
        if vertex not in self.graph:                
            self.graph[vertex] = []                  

    def add_edge(self, src, dest):
        self.addVertex(src)                          
        self.addVertex(dest)
        self.graph[src].append(dest)                 
        self.graph[dest].append(src)

    def display_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
            
if __name__ == "__main__":
    G = Graph()
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('B', 'C')
    G.add_edge('C', 'D')
    G.display_graph()

