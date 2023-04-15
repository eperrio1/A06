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



    
    def test_numberOfLeaves(self):
        proud_tree = Tree('Penny')
        proud_tree.left = Tree('Trudy')
        proud_tree.right = Tree('Oscar')  
        self.assertEqual(2, proud_tree.numberOfLeaves())
        
        annnie_tree = Tree("Annie")
        self.assertEqual(1, annnie_tree.numberOfLeaves())


    
    def test_find(self):
        proud_tree = Tree('Penny')
        proud_tree.left = Tree('Trudy')
        proud_tree.right = Tree('Oscar') 
        
        self.assertEqual(proud_tree, proud_tree.find("Penny"))
        self.assertEqual("Bebe", proud_tree.find("Bebe"))      
    

    
        



if __name__ == "__main__":
    unittest.main()