class Object:
    def __init__(self, value):
        self.value = value
        self.stack = list()
        self.size = 0
    def add(self, value):
        self.stack.append(value)
        print("New Stack: " + str(self.stack))
        print(" ")
        self.size += 1
    def remove(self):
        if len(self.stack) > 0:
            print("Popped Value: " + str(self.stack.pop()))
            print("New Stack: " + str(self.stack))
            print(" ")
            self.size = self.size - 1
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            print(self.stack[len(self.stack) - 1])
        else:
            return None
    def get_size(self):
        return self.size


object = Object(0)
object.add(2)
object.add(6)
object.add(10)
print(object.get_size())
print(" ")
object.remove()
object.remove()




