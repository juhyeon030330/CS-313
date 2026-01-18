class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        ######## YOUR CODE STARTS HERE ######
        # raise NotImplementedError()
        self.root = None

    def insert(self, value):
        ######## YOUR CODE STARTS HERE ######
        # raise NotImplementedError()
        self.root = self.insert_helper(self.root, value)
    
    def insert_helper(self, node, value):
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self.insert_helper(node.left, value)
        else:
            node.right = self.insert_helper(node.right, value)

        return node

    def delete(self, value):
        ######## YOUR CODE STARTS HERE ######
        # raise NotImplementedError()
        self.root = self.delete_helper(self.root, value)

    def delete_helper(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self.delete_helper(node.left, value)
        elif value > node.value:
            node.right = self.delete_helper(node.right, value)
        
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                right_min = self.find_min(node.right)
                node.value = right_min.value
                node.right = self.delete_helper(node.right, right_min.value)
        
        return node
    
    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find(self, value):
        ######## YOUR CODE STARTS HERE ######
        # raise NotImplementedError()
        cur = self.root
        while cur:
            if cur.value < value:
                cur = cur.right
            elif cur.value > value:
                cur = cur.left
            else:
                return True
        return False
            

    def inorder_traversal(self):
        ######## YOUR CODE STARTS HERE ######
        # raise NotImplementedError()
        return self.inorder_traversal_helper(self.root)
    
    def inorder_traversal_helper(self, node):
        if node is None:
            return []
        else:
            return (
                self.inorder_traversal_helper(node.left)
                + [node.value]
                + self.inorder_traversal_helper(node.right)
            )