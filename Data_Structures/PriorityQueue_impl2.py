import copy


def minHeapComparator(firstElement, secondElement):
    return firstElement - secondElement


def maxHeapComparator(firstElement, secondElement):
    return secondElement - firstElement


class PQNode:
    def __init__(self, data=None, priority: int = 0, pos: int = 0):
        self.content = data
        self.priority = priority
        self.pos = pos

    def setPos(self, pos):
        self.pos = pos

    def compare(self, comparingNode, compareFunc):
        return compareFunc(self.priority, comparingNode.priority)


class PriorityQueueImpl2:
    def __init__(self, compareFunc, root=None, priority=0):
        self.compareFunc = compareFunc
        if not isinstance(root, PQNode):
            self.root = PQNode(data=root, priority=priority)
        elif isinstance(root, PQNode):
            self.root = root

        if self.root is not None:
            self.root.setPos(1)
        firstElement = PQNode()
        self.heap = (list((firstElement, self.root)) if root is not None else [firstElement])  # the heap for
        # the priority queue
        self.size = (1 if root is not None else 0)  # size of the heap

    def parent(self, node: PQNode):
        if node == self.root: return self.root
        return self.heap[int(node.pos / 2)]

    def leftNode(self, node: PQNode):
        if int(node.pos * 2) > self.size:
            return None
        return self.heap[int(node.pos * 2)]

    def rightNode(self, node: PQNode):
        if int((node.pos * 2) + 1) > self.size:
            return None
        return self.heap[int((node.pos * 2) + 1)]

    def isLeaf(self, node: PQNode):
        return node.pos > (self.size / 2)

    def swap(self, node: PQNode, swapPos: int):
        posForOldNode = node.pos
        nodeToSwapOut = self.heap[swapPos]
        node.pos = swapPos
        nodeToSwapOut.pos = posForOldNode
        self.heap[swapPos] = node
        self.heap[posForOldNode] = nodeToSwapOut
        return nodeToSwapOut

    def findNode(self, targetData):
        # print(targetData)
        for node in self.heap:
            # print(node.content)
            if node.content == targetData:
                return node

    def changePriority(self, data, newPriority):
        targetNode = self.findNode(data)
        targetNode_copy = copy.deepcopy(targetNode)
        targetNode_copy.priority = newPriority
        self.remove(targetNode)
        self.insert(targetNode_copy)

    def heapify(self, node: PQNode):
        if not self.isLeaf(node):
            swapPos = node.pos
            if self.rightNode(node) is not None:
                if self.leftNode(node).compare(self.rightNode(node), self.compareFunc) < 0:
                    swapPos = self.leftNode(node).pos
                else:
                    swapPos = self.rightNode(node).pos
            else:
                swapPos = self.leftNode(node).pos

            if self.leftNode(node).compare(node, self.compareFunc) < 0 \
                    or (self.rightNode(node) is not None and self.rightNode(node).compare(node, self.compareFunc) < 0):
                nodeSwappedOut = self.swap(node, swapPos)
                self.heapify(node)

    def insert(self, obj, priority=None):
        node: PQNode
        if isinstance(obj, PQNode):
            node = obj
        elif priority is not None:
            node = PQNode(data=obj, priority=priority)
        else:
            raise ValueError("No priority provided for given data. Cannot insert element if priority of element not "
                             "provided.")

        self.heap.append(node)
        self.size += 1
        node.pos = self.size
        if self.root is None:
            self.root = node
            return
        # print(self.parent(node).priority)
        while node.compare(self.parent(node), self.compareFunc) < 0:
            parentNodeSwappedOut = self.swap(node, self.parent(node).pos)
            if (node.pos == 1):
                break

    def remove(self, node):
        removedPos = node.pos
        self.heap[removedPos] = self.heap[self.size]
        self.heap[removedPos].setPos(removedPos)
        del self.heap[-1]
        self.size -= 1
        self.heapify(self.heap[removedPos])

    def pop(self):
        nextNodeOffTree = self.heap[1]
        content = nextNodeOffTree.content
        self.remove(nextNodeOffTree)
        return content

    def print(self):
        return [o.content for o in self.heap[1:]]


minHeap = PriorityQueueImpl2(minHeapComparator)
minHeap.insert("part1", 12)
minHeap.insert("part2", 3)
minHeap.insert("part3", 5)
minHeap.insert("part4", 35)
minHeap.insert("part5", 65)
minHeap.insert("part6", 101)
minHeap.insert("part7", 65)
minHeap.insert("part8", 3)
minHeap.insert("part9", 23)
minHeap.changePriority("part2", 21)
print(minHeap.print())

pq = minHeap
firstNumberOff = pq.pop()
print(f"Next node off {firstNumberOff} --> New Queue is {pq.print()}")
