from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def path_exists(self, start, end, visited=None):
        if visited is None:
            visited = set()

        if start == end:
            return True

        visited.add(start)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                if self.path_exists(neighbor, end, visited):
                    return True

        return False

# Create the graph and add edges
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 1)
g.add_edge(2, 5)
g.add_edge(5, 2)
g.add_edge(3, 6)
g.add_edge(6, 3)
g.add_edge(6, 4)
g.add_edge(4, 6)
g.add_edge(7, 4)
g.add_edge(4, 7)
g.add_edge(6, 7)
g.add_edge(7, 6)

# User input for two nodes
node1 = int(input("Enter the first node: "))
node2 = int(input("Enter the second node: "))

# Check if a path exists between the two nodes
if g.path_exists(node1, node2):
    print(f"Path exists between {node1} and {node2}.")
else:
    print(f"No path exists between {node1} and {node2}.")