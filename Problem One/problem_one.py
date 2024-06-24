

# .............solution 1st way............
def sumsubmuldivFunction():
    a = int(input())
    b = int(input())
    total = a+b
    print(f"SUM: {total}")

    a2 = int(input())
    b2 = int(input())
    total2 = a-b
    print(f"SUB: {total2}")

    a3 = int(input())
    b3 = int(input())
    total3 = a*b
    print(f"MUL: {total3}")

    a4 = int(input())
    b4 = int(input())
    total4 = a/b
    print(f"DIV: {total3}")
    
sumsubmuldivFunction()




# .............solution 2nd way............
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
print(f"DIV: {div}")







    
