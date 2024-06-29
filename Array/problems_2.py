# Find Only odd sum, means if you are given [1,3,4,5,5,6,7] this array, please find sum of odd numbers 1+3+5.... Nth Odd

def oddSum():
    arr = [1,3,4,5,5,6,7]
    s = 0
    for i in arr:
        if i % 2 != 0:
            s = s + i
    return s

def oddSum_N(N):
    s = 0
    for i in range(1,N+1):
        if i % 2 != 0:
            s = s + i
    return s


#fun 1 
total = oddSum()
print("odd sum is ", total)

#fun 2
total = oddSum_N(9)
print("odd sum of N is ", total)