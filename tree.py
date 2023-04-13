class Tree:

    def __init__(self, node, left=None, right=None):
        self.left = left
        self.right = right

    def is_a_left(self):
        if self.left == None and self.right == None:
            return True
        return False

   