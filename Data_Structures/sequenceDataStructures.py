## Sequence Data Structures
print("Sequence Structures Intro: ")
x = "Hello World"  #String
print(x)
print(" ")

y = ['Surya', 'Satya', 'Shreeya']  #List/Static Array
print(y)
print(" ")

z = ('Surya', 'Satya', 'Shreeya')  #Tuple
print(z)
print(" ")

## Indexing Sequence Structures
print("Indexing Sequence Structures: ")
print(x[0])  #Indexing String x for the first letter (or 0th index)
print(x[4])  #Indexing String x for the fifth letter (or 4th index)
print(" ")

print(y[0])   #Indexing Arrya/List y for the first element (or 0th index)
print(y[1])   #Indexing Arrya/List y for the second element (or 1th index)
print(y[1])   #Indexing Arrya/List y for the second element (or 1th index)
print(" ")

print(z[0])   #Indexing Tuple y for the first element (or 0th index)
print(z[1])   #Indexing Tuple y for the second element (or 1th index)
print(z[1])   #Indexing Tuple y for the second element (or 1th index)
print(" ")

## Slicing Sequence Structures
print("Slicing Sequence Structures: ")
print(x[1:4])  #Slicing String x from the second letter through fifth (or 0 - 4 index)
print(x[:9])  #Indexing String x from the first letter to 10th (or beginning index - 10th index)
print(x[2:])  #Indexing String x from the third letter to last (or 2nd - last index)
print(" ")

print(y[1:2])
print(y[:3])
print(y[2:])
print(" ")

print(z[:1])
print(z[1:])
print(" ")

## Concatenating Sequence Structures
print("Concatenation pf Sequence Structures: ")
x = 'horse' + 'mouse'
print(x)

y = ['Tom', 'Henry'] + ['Sam', 'Ben']
print(y)

z = ('Tom', 'Henry') + ('Sam',) #To concantenate Tuple you must have a comma after the second tuple
print(z)

## Multiplying Sequence Structures
print("Multiplying Sequence Structures: ")
x = 'bug' * 3
print(x)

y = [5, 8] * 4
print(y)

z = ('Hello', 'World') * 3
print(z)
print(" ")

## Checking Membership
print("Checking Membership in Sequence Structures: ")
x = 'bug'
print('u' in x)

y = [5, 8, 10, 7, 8, 56, 79]
print(101 in y)

z = ('Hello', 'World', 'Octopus', 'Joe', 'Ughh')
print('Joe' not in z)
print(" ")

## Iterating Through Items
print("Item Iteration: ")
x = "Hello"
for i in x:
    print(i)

y = [34, 67, 89, 100, 23, 45]
for item in y:
    print(item)

print(' ')

## Enumeration
print("Item Enumeration: ")
x = [45, 67, 34, 2]
for index,element in enumerate(x):
    print(index, element)
print(" ")

y = ('Python', 'is', 'cool', '!')
for index,element in enumerate(y):
    print(index, element)
print(" ")

## Unpacking Arrays/List
print("Unpacking Arrays/List: ")
x = ['bob', 'bill', 'joe']
a, b, c, = x
print(a, b, c)





