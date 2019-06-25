import array
a = 2
b = 3
print(a+b)

arr = array.array("i", [90,89,76,56])
for i in range(0,len(arr)):
    print(arr[i], end=" ")

r = len(arr)
for r in range(len(arr), 12):
    t = arr[r - 1] + 1
    print(t)
    print(arr.append(t))

print(arr)
        
