class Graph:
    def __init__(self):
        self.graph = {}                             

    def add_vertex(self, vertex):
        if vertex not in self.graph:                
            self.graph[vertex] = []                 

    def addEdge(self, src, dest):
        self.add_vertex(src)                         
        self.add_vertex(dest)
        self.graph[src].append(dest)                
        self.graph[dest].append(src)

    def display_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs_visited(self, vertex, visited):
        visited.add(vertex)                         
        print(vertex, end=" ")                      

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:             
                self.dfs_visited(neighbor, visited) 

    def dfs(self, start_vertex):
        visited = set()                             
        self.dfs_visited(start_vertex, visited)     

if __name__ == "__main__":
    G = Graph()
    G.addEdge('A', 'B')
    G.addEdge('A', 'C')
    G.addEdge('B', 'C')
    G.addEdge('C', 'D')

    G.display_graph()
    print("DFS traversal starting from vertex A:")
    G.dfs('A')
    print("\nDFS traversal starting from vertex B:")
    G.dfs('B')
    print("\nDFS traversal starting from vertex C:")
    G.dfs('C')
    print("\nDFS traversal starting from vertex D:")
    G.dfs('D')