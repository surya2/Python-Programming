import copy


def minHeapComparator(firstElement, secondElement):
    return firstElement - secondElement


def maxHeapComparator(firstElement, secondElement):
    return secondElement - firstElement


class Node:
    def __init__(self, innerContent=None, metadata=None, pos: int = 0):
        self.content = innerContent
        self.metadata = metadata
        self.pos = pos

    def compare(self, comparingNode, compareFunc):
        if isinstance(self.content, int):
            return compareFunc(self.content, comparingNode.content)


class Heap:
    def __init__(self, compareFunc, root: Node = None):
        self.compareFunc = compareFunc
        self.root = root
        self.root.pos = 1 if self.root is not None else None
        self.heap = (list((object, self.root)) if self.root is not None else list(object))
        self.size = (1 if self.root is not None else 0)

    def parent(self, node: Node):
        if node == self.root: return self.root
        return self.heap[int(node.pos / 2)]

    def leftNode(self, node: Node):
        return self.heap[int(node.pos * 2)]

    def rightNode(self, node: Node):
        return self.heap[int((node.pos * 2) + 1)]

    def isLeaf(self, node: Node):
        return node.pos > (self.size / 2)

    def swap(self, node: Node, swapPos: int):
        posForOldNode = node.pos
        nodeToSwapOut = self.heap[swapPos]
        node.pos = swapPos
        nodeToSwapOut.pos = posForOldNode
        self.heap[swapPos] = node
        self.heap[posForOldNode] = nodeToSwapOut
        return nodeToSwapOut

    def heapify(self, node: Node):
        if not self.isLeaf(node):
            swapPos = node.pos
            if self.rightNode(node) is not None:
                if self.leftNode(node).compare(self.rightNode(node), self.compareFunc) < 0:
                    swapPos = self.leftNode(node).pos
                else:
                    swapPos = self.rightNode(node).pos
            else:
                swapPos = self.leftNode(node).pos

            if self.leftNode(node).compare(node, self.compareFunc) < 0 or self.rightNode(node).compare(node,
                                                                                                       self.compareFunc) < 0:
                nodeSwappedOut = self.swap(node, swapPos)
                self.heapify(node)

    def insert(self, obj, metadata=None):
        node: Node
        if isinstance(obj, Node):
            node = obj
        else:
            node = Node(innerContent=obj, metadata=metadata)

        self.heap[self.size + 1] = node
        self.size += 1
        node.pos = self.size
        while node.compare(self.parent(node), self.compareFunc) < 0:
            parentNodeSwappedOut = self.swap(node, self.parent(node).pos)

    def remove(self, node):
        removedPos = node.pos
        self.heap[removedPos] = self.heap[self.size]
        self.size -= 1
        self.heapify(self.heap[removedPos])
