from tree import Tree
def main():
    randomly_generate_tree = build_random_tree(6)

    family_tree = Tree('Elana')
    family_tree.left = Tree('Frederica')
    family_tree.left.left = Tree('Erma')
    family_tree.left.right = Tree('Louis')
    family_tree.left.right.left = Tree("Golden")
    
    family_tree.right = Tree('Godfrey')
    family_tree.right.left = Tree("Nita")
    family_tree.right.left.left = Tree("Elly")
    family_tree.right.left.right = Tree("Frank")
    
    family_tree.right.right = Tree("Tony")
    family_tree.right.right.right = Tree("Godfrey")
    family_tree.right.right.left = Tree("Bernice")
    print(family_tree)

def build_random_tree(m):
    # for i in m:
        # call method to grow tree 
    # return tree 
    return m

if __name__ == "__main__":
    main()