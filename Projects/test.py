import math

print('Qudratic Equation Calculator')
print()

a = input('What is your first value for A? ')
b = input('What is your first value for B? ')
c = input('What is your first value for C? ')

def calc(first, second, third):
    prov1 = math.sqrt((second**2) - ((4*first)*third))
    prov2 = -1 * b
    root1 = (prov2 + prov1)/(2*first)
    root2 = (prov2 - prov1)/(2*first)
    return(root1, root2)

ans = calc(a, b, c)
print("Your Quadratic Roots Are: " + ans)

