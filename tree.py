class Tree:

    def __init__(self, node, left=None, right=None):
        self.left = left
        self.right = right
        self.node = node


    def find(self, value):
        if self.node == value:
            return self
            
        if self.node != value and self.right is not None:
            return self.right.find(value)

        if self.node != value and self.left is not None:
            return self.left.find(value)
        
        return value

    def FullBinaryTree(self):
        if self.numberOfLeaves() % 2 == 0:
            return True
        else:
            return False

    def is_leaf(self):
        if self is None:
            return True
        if self.left is None and self.right is None:
            return True
        return False

    
    def insert(self, node):
        if self.node == node:
            return self
            
        if self is None: 
            return Tree(node)

            
        # if self.left is None:
            # self.left = Tree(node)
            # return self.left.insert(node)
 

        if self.right is None:
            self.right = Tree(node)
            return self.right.insert(node)
 
            
        return self

    def numberOfLeaves(self):
        if self.is_leaf() == True:
            return 1  
       
        if self is None:
            return 0 

        if self.right is not None and self.left is not None:
            return self.right.numberOfLeaves() + self.left.numberOfLeaves()

        if self.right is not None:
            return self.right.numberOfLeaves()

        if self.left is not None:
            return self.left.numberOfLeaves()        


    def output(self, indents):
        display = '\t'* indents + self.node 
        if self.left is not None:
            display += '\n' + '\t' * indents + self.left.output(indents + 1) 
        if self.right is not None:
            display += '\n' + '\t' * indents + self.right.output(indents + 1) 
        return display

    def __str__(self):
        return self.output(0)
       
        