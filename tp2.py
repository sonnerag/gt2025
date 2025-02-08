from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices + 1)] for _ in range(vertices + 1)]  # +1 to handle 1-based indexing
    
    def add_edge(self, u, v):
        self.graph[u][v] = 1
    
    def DFS(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for i in range(1, self.V + 1):  # Iterate from 1 to V
            if self.graph[v][i] == 1 and not visited[i]:
                self.DFS(i, visited, component)
    
    def get_transpose(self):
        transposed_graph = Graph(self.V)
        for i in range(1, self.V + 1):
            for j in range(1, self.V + 1):
                transposed_graph.graph[i][j] = self.graph[j][i]
        return transposed_graph
    
    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in range(1, self.V + 1):
            if self.graph[v][i] == 1 and not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(v)
    
    def get_strongly_connected_components(self):
        stack = []
        visited = [False] * (self.V + 1)  # +1 to handle 1-based indexing
        
        # Fill vertices in stack according to their finishing times
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.fill_order(i, visited, stack)
        
        # Create a reversed graph
        transposed_graph = self.get_transpose()
        
        # Mark all vertices as not visited (for second DFS)
        visited = [False] * (self.V + 1)
        
        # Now process all vertices in order defined by stack
        sccs = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                transposed_graph.DFS(i, visited, component)
                sccs.append(component)
        return sccs
    
    def get_weakly_connected_components(self):
        visited = [False] * (self.V + 1)  # +1 to handle 1-based indexing
        wccs = []
        
        for i in range(1, self.V + 1):
            if not visited[i]:
                component = []
                self.DFS(i, visited, component)
                wccs.append(component)
        
        return wccs

# Example usage:
if __name__ == "__main__":
    # Create a graph with 9 vertices (1 to 9)
    g = Graph(9)
    
    # Add edges as per the input
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 3)
    g.add_edge(5, 5)
    g.add_edge(5, 4)
    g.add_edge(5, 9)
    g.add_edge(7, 3)
    g.add_edge(7, 8)
    g.add_edge(7, 5)
    g.add_edge(7, 6)
    g.add_edge(8, 3)
    g.add_edge(8, 9)
    
    print("Weakly Connected Components:")
    wccs = g.get_weakly_connected_components()
    print(wccs)
    print("Number of Weakly Connected Components:", len(wccs))
    
    print("\nStrongly Connected Components:")
    sccs = g.get_strongly_connected_components()
    print(sccs)
    print("Number of Strongly Connected Components:", len(sccs))