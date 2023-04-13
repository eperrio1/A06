class Tree:

    def __init__(self, node, left=None, right=None):
        self.left = left
        self.right = right

    def is_a_leaf(self):
        if self.left == None and self.right == None:
            return True
        return False

    def numberOfLeaves(self):
        if self.is_a_left() == True:
            count += 1
            return count

        if self.left is not None:
            return self.left.numebrOfLeaves(count)

        if self.right is not None:
            return self.right.numberOfLeaves(count)

       
        