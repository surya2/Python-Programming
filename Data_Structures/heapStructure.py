class maxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
    def peek(self):
        return self.heap[1]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def floatUp(self, index):  #Index is child here
        parent = index/2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.floatUp(parent)
        else:
            return
    def bubbleDown(self, index):  #Index in parents here
        leftChild = index *2
        rightChild = index*2+1
        larger = index
        if len(self.heap) > leftChild and self.heap[larger] < self.heap[leftChild]:
            larger = leftChild
        if len(self.heap) > rightChild and self.heap[larger] < self.heap[rightChild]:
            larger = rightChild
        if larger != index:
            self.swap(index, larger)
            self.bubbleDown(larger)