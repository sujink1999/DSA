# Implementation of Fenwick Tree - Range Query

def getSum(BITree: list, index: int) -> int:
    summ = 0 
    index = index + 1
    while index > 0:
        summ += BITree[index] 
        index -= index & (-index)
    return summ

print(getSum([0,1,2,3,4,5,6], 2))