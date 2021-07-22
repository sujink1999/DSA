# Implementation of Fenwick Tree - Range Query (Binary Indexed Tree)

class BIT:
    def __init__(self, arr):
        self.bITree = [0] * (len(arr)+1)
        for i, val in enumerate(arr):
            self.update(i, val)

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
        
    def update(self, index, val):
        index+=1
        while index < len(self.bITree):
            self.bITree[index] += val

            # TO GET THE NEXT INDEX TO UPDATE
            # Take 2's complement. AND to the orginal value. Add the original value
            index += self.lsb(index)


# Driver code
bit = BIT([1,5,1,1,10])
print(bit.getSum(2))