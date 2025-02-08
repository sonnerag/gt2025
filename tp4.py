import sys

# Provided adjacency matrix
adj_matrix = [
    [0, 4, 0, 0, 1, 0, 2, 0, 0],
    [4, 0, 7, 0, 0, 5, 0, 0, 0],
    [0, 7, 0, 1, 0, 8, 0, 0, 0],
    [0, 0, 1, 0, 0, 6, 4, 3, 0],
    [1, 0, 0, 0, 0, 9, 10, 0, 0],
    [0, 5, 8, 6, 9, 0, 0, 0, 2],
    [2, 0, 0, 4, 10, 0, 2, 0, 8],
    [0, 0, 0, 3, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 2, 8, 1, 0]
]

# Prim's Algorithm
def prim_mst(adj_matrix, root):
    num_nodes = len(adj_matrix)
    key = [sys.maxsize] * num_nodes  # Key values used to pick minimum weight edge
    parent = [None] * num_nodes      # Array to store the MST
    key[root-1] = 0                  # Start with the root node
    mst_set = [False] * num_nodes    # Track nodes included in MST

    for _ in range(num_nodes):
        # Find the node with the minimum key value that is not yet in the MST
        u = min_key(key, mst_set)
        mst_set[u] = True  # Add the node to the MST set

        # Update key values and parent for adjacent nodes
        for v in range(num_nodes):
            if adj_matrix[u][v] > 0 and not mst_set[v] and adj_matrix[u][v] < key[v]:
                key[v] = adj_matrix[u][v]
                parent[v] = u

    return parent, key

def min_key(key, mst_set):
    min_val = sys.maxsize
    min_index = -1

    for v in range(len(key)):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v

    return min_index

def print_mst_prim(parent, key):
    print("\nPrim's Minimal Spanning Tree:")
    print("Edge \tWeight")
    weighted_sum = 0
    for i in range(len(parent)):
        if parent[i] is not None:  # Skip the root node (it has no parent)
            print(f"{parent[i]+1} - {i+1} \t{key[i]}")
            weighted_sum += key[i]
    print(f"Weighted Sum of MST: {weighted_sum}")

# Kruskal's Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sort edges by weight
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("\nKruskal's Minimal Spanning Tree:")
        print("Edge \tWeight")
        weighted_sum = 0
        for u, v, weight in result:
            print(f"{u+1} - {v+1} \t{weight}")
            weighted_sum += weight
        print(f"Weighted Sum of MST: {weighted_sum}")

# Main script
if __name__ == "__main__":
    # Ask user for the root node for Prim's Algorithm
    root_node = int(input("Enter the root node for Prim's Algorithm (1-9): "))
    if root_node < 1 or root_node > 9:
        print("Invalid root node. Please enter a number between 1 and 9.")
    else:
        # Run Prim's Algorithm
        parent, key = prim_mst(adj_matrix, root_node)
        print_mst_prim(parent, key)

        # Run Kruskal's Algorithm
        g = Graph(9)
        for u in range(9):
            for v in range(u + 1, 9):
                if adj_matrix[u][v] > 0:
                    g.add_edge(u, v, adj_matrix[u][v])
        g.kruskal_mst()