from collections import deque

queue = deque()

queue.append(5)
queue.append(7)
queue.append(9)
print(queue)
print(queue.popleft())
print(queue)
queue.append(10)
print(queue)
print(queue.popleft())
