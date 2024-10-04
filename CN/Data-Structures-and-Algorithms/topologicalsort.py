#TOPOLOGICAL SORT
def topo_sort(vertices, edges):
    in_degree = [0] * vertices
    adj_list = [[] for _ in range(vertices)]
    
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1
    

    result = []
    zero_in_degree = [i for i in range(vertices) if in_degree[i] == 0]
    
    while zero_in_degree:
        u = zero_in_degree.pop(0)  
        result.append(u)
        
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:  
                zero_in_degree.append(v)
    
    
    if len(result) == vertices:
        return result
    else:
        return "Graph has a cycle, topological sort not possible."
vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

edges = []
for _ in range(num_edges):
    u, v = map(int, input("Enter an edge (u v): ").split())
    edges.append((u, v))
print("Topological Sort:", topo_sort(vertices, edges))
