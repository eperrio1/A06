class Tree:

    def __init__(self, node, left=None, right=None):
        self.left = left
        self.right = right
        self.node = node

    # need to test
    def is_leaf(self):
        if self is None:
            return True
        if self.left is None and self.right is None:
            return True
        return False

    # need to test
    def numberOfLeaves(self):
        if self.is_leaf() == True:
            count += 1
            return count

        if self.left is not None:
            return self.left.numebrOfLeaves(count)

        if self.right is not None:
            return self.right.numberOfLeaves(count)

    def output(self, indents):
        display = '\t'* indents + self.node 
        if self.left is not None:
            display += '\n' + '\t' * (indents + 1) + self.left.output(indents + 1) 
        if self.right is not None:
            display += '\n' + '\t' * (indents + 1) + self.right.output(indents + 1) 
        return display

    def __str__(self):
        return self.output(0)
       
        