from Exercise19_5 import BST


numbers = [2, 4, 3, 1, 8, 5, 6, 7]
intTree = BST()
for e in numbers:
    intTree.insert(e)
    
print("\nInorder recursive (sorted): ", end = "")
intTree.inorder()

print("\nInorder iterative (sorted): ", end = "")
intTree.inorder_iterative()

print("\nPostorder recursive: ", end = "")
intTree.postorder()

print("\nPostorder iterative: ", end = "")
intTree.postorder_iterative()

print("\nPreorder recursive: ", end = "")
intTree.preorder()

print("\nPreorder iterative: ", end = "")
intTree.preorder_iterative()