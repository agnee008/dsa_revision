from collections import deque, defaultdict

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def bottom_view(root):
    if not root:
        return

    # Dictionary to store the bottom view of the binary tree
    bottom_view_dict = defaultdict(int)

    # Queue for level-order traversal (node, horizontal distance)
    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()
        
        # Overwrite the value at horizontal distance hd
        bottom_view_dict[hd] = node.key
        
        # If there is a left child, add it to the queue
        if node.left:
            queue.append((node.left, hd - 1))
        
        # If there is a right child, add it to the queue
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Extract the bottom view from the dictionary
    for hd in sorted(bottom_view_dict):
        print(bottom_view_dict[hd], end=' ')

# Helper function to create a binary tree
def create_binary_tree():
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)
    return root

# Example usage
if __name__ == "__main__":
    root = create_binary_tree()
    print("Bottom view of the binary tree is:")
    bottom_view(root)
