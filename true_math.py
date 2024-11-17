from math import inf
def divide(first, sekond):
    result= (first, sekond)
    if sekond ==(0):
       return inf


    else:
        return result

result1 =  divide(12, 4)
result2 =  divide(12, 0)
print(result1)
print(result2)