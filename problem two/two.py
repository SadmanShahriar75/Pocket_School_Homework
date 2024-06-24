#fun oddsum
def oddSum():
    print("OddSum")
    n = int(input("input: "))
    s = 0
    for i in range(0, n+1):
        if i % 2  == 0 :
            s = s + i
    return s

#fun evensum
def evenSum():
    print("EvenSum")
    n = int(input("input: "))
    s = 0
    for i in range(0, n+1):
        if i % 2  == 1 :
            s = s + i
    return s

#call the oodsum sun
final = oddSum()
print("output:", final)
print()

#now call the evensum
final2 = evenSum()
print("output:", final2)
print()

#for invalid range
n = int(input("input: "))
if n>1000:
    print("output:", "invalid range")