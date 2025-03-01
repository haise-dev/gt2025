def construct_adj_matrix(edges, numOfNodes):
    adj_matrix = []
    for _ in range(numOfNodes):
        numberOfRow = [0] * numOfNodes
        adj_matrix.append(numberOfRow)

    for u, v in edges:
        if 1 <= u <= numOfNodes and 1 <= v <= numOfNodes:
            adj_matrix[u - 1][v - 1] = 1  # for directed Graph
            # adj_matrix[v - 1][u - 1] = 1 # for undirected Graph
    else:
        print(f"Invalid edge: ({u}, {v})")

    return adj_matrix


edges = [
    (1, 2), (1, 3), (2, 5), (2, 6),
    (3, 4), (4, 8), (5, 7)
]
num_nodes = 8

adjacency_matrix = construct_adj_matrix(edges, num_nodes)

print("a) Construct Adjacent Matrix for graph G:")
for row in adjacency_matrix:
    print(row)


class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def inorderTraversal(root):

    if root is None:
        return

    inorderTraversal(root.left)
    print(root.label, end=" ")
    inorderTraversal(root.right)


def findSubtree(root, x):

    if root is None:
        return None

    if root.label == x:
        return root

    left_result = findSubtree(root.left, x)
    if left_result:
        return left_result
    return findSubtree(root.right, x)


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)

    root.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(7)

x = int(input("b) Inorder Algorithm: Enter the root label of the subtree to traverse (inorder): "))

subtree_root = findSubtree(root, x)
if subtree_root:
    print(f"Inorder traversal of subtree rooted at node {x}:")
    inorderTraversal(subtree_root)
else:
    print(f"Node {x} not found in the tree.")
