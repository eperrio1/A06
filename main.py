from tree import Tree
from binarySearchTree import BinarySearchTree
import random  

def main():
       

    print('Elana\'s family Tree')
    family_tree = Tree('Elana')
    family_tree.left = Tree('Frederica')
    family_tree.left.left = Tree('Erma')
    family_tree.left.left.left = Tree('Sarah')
    family_tree.left.left.right= Tree('James')

    family_tree.left.right = Tree('Louis')
    family_tree.left.right.left = Tree('Golden')
    family_tree.left.right.right = Tree('Joseph')
    
    family_tree.right = Tree('Godfrey')
    family_tree.right.left = Tree('Anita')
    family_tree.right.left.left = Tree('Miriam')
    family_tree.right.left.right = Tree('Frank')
    
    family_tree.right.right = Tree('Godfrey')
    family_tree.right.right.right = Tree('Godfrey')
    family_tree.right.right.left = Tree('Bernice')
    print(family_tree)


    print(f'\n How many leaves are in the family tree?')
    print(family_tree.numberOfLeaves())

    print(f"\nIs this following name in the family tree?")
    print(f'Elana:\n {family_tree.find("Elana")}')

    print(f'\n Is the family tree a full tree?')
    print(family_tree.FullBinaryTree())

    # randomly_generate_tree = build_random_tree(6)
    # print(randomly_generate_tree)

    # test = Tree("Elana")
    # test = test.insert("Eleia")
    # test = test.insert("Elisa")
    # print(test)

    randomly_generate_BST = build_random_binary_search_tree(6)
    print(randomly_generate_BST)
 
    
# Come back to this
def build_random_tree(m):
    list_names = ["Elana", "Elisa", "Eleia", "Dajah", "James", "Madison"]
    tree = Tree(random.choice(list_names))
    
    for i in range(m):
        tree.insert(random.choice(list_names))
       
    return Tree

# Come back to this
def build_random_binary_search_tree(n):
    tree = BinarySearchTree(random.randint(1, 10))
    for i in range(n):
        tree.insert(random.randint(1, 10))
    return tree
        
if __name__ == "__main__":
    main()