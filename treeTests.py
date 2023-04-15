import unittest
from tree import Tree  

class treeTests(unittest.TestCase):
    
    def test_is_leaf(self):
        proud_tree = Tree('Penny')
        proud_tree.left = Tree('Trudy')
        proud_tree.right = Tree('Oscar')
        self.assertEqual(False, proud_tree.is_leaf())
        self.assertEqual(True, proud_tree.right.is_leaf())
        self.assertEqual(True, proud_tree.left.is_leaf())
        



if __name__ == "__main__":
    unittest.main()