def inorder_traversal(adj_matrix, x, nodes):
    """
    Perform Inorder traversal on the subtree rooted at node x.
    :param adj_matrix: Adjacency matrix of the graph.
    :param x: The root node of the subtree.
    :param nodes: List of all nodes in the graph.
    """
    # Find all children of x
    children = [i for i, val in enumerate(adj_matrix[x - 1]) if val == 1]
    
    # Base case: If no children, print the node and return
    if not children:
        print(x, end=" ")
        return
    
    # Traverse the leftmost child (first child)
    if children:
        inorder_traversal(adj_matrix, children[0] + 1, nodes)
    
    # Print the current node
    print(x, end=" ")
    
    # Traverse the remaining children
    for child in children[1:]:
        inorder_traversal(adj_matrix, child + 1, nodes)

# Adjacency matrix for the graph
adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 1, 1, 0, 0],  
    [0, 0, 0, 1, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 1],  
    [0, 0, 0, 0, 0, 0, 1, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
]

# List of all nodes
nodes = [1, 2, 3, 4, 5, 6, 7, 8]

# Input: Node label (x)
x = int(input("Enter the node label (x): "))

# Perform Inorder traversal on the subtree rooted at x
print(f"Inorder traversal of subtree rooted at {x}:")
inorder_traversal(adj_matrix, x, nodes)