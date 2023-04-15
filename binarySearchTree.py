class BinarySearchTree:

    def __init__(self, node, left=None, right=None):
        self.right = right
        self.left = left
        self.node = node


    def insert(self, node):
        print(self)
        if node is None:
            return BinarySearchTree(node)

        if node < self.node:
            self.left = self.insert(node)
            
        else:        
            self.right = self.insert(node)
        
        return self