def sumFunction():
    a = int(input())
    b = int(input())
    total = a+b
    return total
def subFunction():
    a = int(input())
    b = int(input())
    total = a-b
    return total
def mulFunction():
    a = int(input())
    b = int(input())
    total = a*b
    return total
def divFunction():
    a = int(input())
    b = int(input())
    total = a/b
    return total
summ = sumFunction()
print(f"SUM: {summ}")
subb = subFunction()
print(f"SUB: {subb}")
mul = mulFunction()
print(f"MUL: {mul}")
div = divFunction()
print(f"Div: {div}")



