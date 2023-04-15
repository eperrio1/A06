class Tree:

    def __init__(self, node, left=None, right=None):
        self.left = left
        self.right = right
        self.node = node


    def is_leaf(self):
        if self is None:
            return True
        if self.left is None and self.right is None:
            return True
        return False

    def numberOfLeaves(self):
        if self.is_leaf() == True:
            return 1  
       
        if self is None:
            return 0 

        if self.right is not None and self.left is not None:
            return self.right.numberOfLeaves() + self.left.numberOfLeaves()



    def output(self, indents):
        display = '\t'* indents + self.node 
        if self.left is not None:
            display += '\n' + '\t' * indents + self.left.output(indents + 1) 
        if self.right is not None:
            display += '\n' + '\t' * indents + self.right.output(indents + 1) 
        return display

    def __str__(self):
        return self.output(0)
       
        