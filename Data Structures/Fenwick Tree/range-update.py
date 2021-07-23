# Implementation of Fenwick Tree - Range Update (Binary Indexed Tree)

class BIT:
    def __init__(self, n):
        self.bITree = [0] * (n+1)

    def getSum(self, index):
        summ = 0 
        index = index + 1
        while index > 0:
            summ += self.bITree[index]

            # TO GET THE PARENT 
            # Take 2's complement. AND to the orginal value. Subtract from the original value
            index -= self.lsb(index)
        return summ

    def lsb(self, val):
        return val & (-val)

    def updateRange(self, left, right, val):
        self.update(left, val)
        self.update(right+1, -1 * val)

    def getElement(self, index):
        return self.getSum(index)       
        
    def update(self, index, val):
        index+=1
        while index < len(self.bITree):
            self.bITree[index] += val

            # TO GET THE NEXT INDEX TO UPDATE
            # Take 2's complement. AND to the orginal value. Add the original value
            index += self.lsb(index)


# Driver code
bit = BIT(6)
bit.updateRange(0,3,10)
bit.updateRange(0,2,-5)
bit.updateRange(3,4,2)
print(bit.getElement(4))

# When an array is the input, two trees are maintained, one for the actual array (BIT1) and the other for 
# the range updates (BIT2). Therefore getElement(i) is arr[i] + getSum(BIT2, i) 

# 5 5 5 12 2

