from binarytree import Node

root = Node(15)

root.left = Node(8)
root.right = Node(24)
root.left.left = Node(5)
root.left.right = Node(11)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.left.right.right = Node(13)

root.right = Node(24)
root.right.left = Node(19)
root.right.right = Node(28)
root.right.right.left = Node(25)

print(root)