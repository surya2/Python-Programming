import math
import copy


class Node:
    def __init__(self, innerContent=None, leftNode=None, rightNode=None, metadata=None):
        self.content = innerContent
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.metadata = metadata

    def setLeftNode(self, leftNode):
        self.leftNode = leftNode

    def setRightNode(self, rightNode):
        self.rightNode = rightNode

    def compare(self, nodeToCompare):
        if isinstance(self.content, int):
            return self.content - nodeToCompare.content


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def printRoot(self):
        print(self.root.content, self.root.metadata)

    def add(self, obj, metadata=None):
        # if(currComparingNode == None): currComparingNode = self.root
        if isinstance(obj, Node):
            if self.root is None:
                self.root = obj
                return
            self.addNode(obj, self.root)
        else:
            newNode = Node(obj, metadata=metadata)
            if self.root is None:
                self.root = newNode
                return
            self.addNode(newNode, self.root)

    def addNode(self, node: Node, currComparingNode):
        if node.compare(currComparingNode) <= 0:
            if currComparingNode.leftNode is None:
                currComparingNode.setLeftNode(node)
                return
            self.addNode(node, currComparingNode.leftNode)
        elif node.compare(currComparingNode) > 0:
            if currComparingNode.rightNode is None:
                currComparingNode.setRightNode(node)
                return
            self.addNode(node, currComparingNode.rightNode)

    def remove(self, content, metadata=None):
        self.removeNode(content, metadata, self.root)

    def removeNode(self, content, metadata, currComparingNode):
        if (content < currComparingNode.content) or (
                content == currComparingNode.content and metadata != currComparingNode.metadata):
            self.removeNode(content, metadata, currComparingNode=currComparingNode.leftNode)
        elif content > currComparingNode.content:
            self.removeNode(content, metadata, currComparingNode=currComparingNode.rightNode)
        elif currComparingNode.content == content and currComparingNode.metadata == metadata:
            removedNode = copy.deepcopy(currComparingNode)
            currComparingNode = currComparingNode.rightNode
            self.addNode(removedNode.leftNode, currComparingNode=currComparingNode)
            return removedNode
        else:
            return None


def BinarySearch(content, tree: BinaryTree, metadata=None, comparingNode=None):
    if comparingNode is None: comparingNode = tree.root

    if content < comparingNode.content:
        BinarySearch(content, metadata, comparingNode=comparingNode.leftNode)
    elif content > comparingNode.content:
        BinarySearch(content, metadata, comparingNode=comparingNode.rightNode)
    elif comparingNode.content == content and metadata == None:
        return comparingNode
    elif comparingNode.content == content and metadata == comparingNode.metadata:
        return comparingNode
    else:
        return None


def inOrderTraversal(tree: BinaryTree):
    inOrder(tree, tree.root)


def inOrder(tree, currentNode):
    if currentNode.leftNode is not None:
        inOrder(tree, currentNode.leftNode)
    print(currentNode.content, " ")
    if currentNode.rightNode is not None:
        inOrder(tree, currentNode.rightNode)


b_tree = BinaryTree()
b_tree.add(2, "first node")
b_tree.add(10)

inOrderTraversal(b_tree)

b_tree.printRoot()
