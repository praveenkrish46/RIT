class Graph:
    def __init__(self):
        self.graph = {}                              

    def add_vertex(self, vertex):
        if vertex not in self.graph:                 
            self.graph[vertex] = []                  

    def add_edge(self, src, dest):
        self.add_vertex(src)                          
        self.add_vertex(dest)
        
        self.graph[src].append(dest)                 
        self.graph[dest].append(src)

    def display_Graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def bfs(self, start_vertex):
        visited = set()                               
        queue = []                                    

        queue.append(start_vertex)                    
        visited.add(start_vertex)                     

        while queue:
            vertex = queue.pop(0)                     
            print(vertex, end=" ")                    

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:           
                    queue.append(neighbor)            
                    visited.add(neighbor)             

if __name__ == "__main__":
    G = Graph()
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('B', 'C')
    G.add_edge('C', 'D')

    G.display_Graph()

    print("\nBFS traversal start from vertex A:")
    G.bfs('B')
    print("\nBFS traversal start from vertex B:")
    G.bfs('A')
    print("\nBFS traversal start from vertex C:")
    G.bfs('C')
    print("\nBFS traversal start from vertex D:")
    G.bfs('D')