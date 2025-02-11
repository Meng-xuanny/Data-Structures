import random


class Array():
    def __init__(self,initialSize):
        self._a=[None] * initialSize
        self._nItems=0

    def __len__(self):
        return self._nItems

    def insert(self,item):
        if self._nItems >= len(self._a):
            # raise Exception("Array overflow")
            self.grow()
        self._a[self._nItems]=item
        self._nItems+=1

    def find(self,item):
        for i in range(self._nItems):
            if self._a[i]==item:
                return i
        return -1

    def delete(self,item):
        for i in range(self._nItems):
            if self._a[i] == item:
                for k in range(i,self._nItems-1):
                    self._a[k]=self._a[k+1]

                self._a[self._nItems - 1] = None
                # print(self._a)
                self._nItems -= 1
                return True
        return False

    def grow(self):
        oldSize=len(self._a)
        newSize=oldSize * 2
        newA=[None]*newSize
        for i in range(oldSize):
            newA[i]=self._a[i]
        self._a=newA

    def bubbleSort(self):
        outIteration=0
        innnerIteration=0
        for j in range(self._nItems-1, 0, -1):
            outIteration+=1
            for k in range(j):
                innnerIteration+=1
                if self._a[k]>self._a[k+1]:
                    temp = self._a[k]
                    self._a[k]=self._a[k+1]
                    self._a[k + 1]=temp

        print(outIteration+innnerIteration)

    def selectionSort(self):
        outIteration = 0
        innnerIteration = 0
        for i in range(self._nItems-1): # no need to compare with the last element itself
            outIteration+=1
            min = i # the outter loop keeps iterating until the last element
            for k in range(i+1, self._nItems):
                innnerIteration+=1
                if self._a[k] < self._a[min]:
                    min=k  #store the index of the smallest element to min
        # after i has been compared to all elements and the smallest has been found
        # swap position with the smallest element
            temp=self._a[i]
            self._a[i]=self._a[min]
            self._a[min]=temp

        print(outIteration+innnerIteration)


    def insertionSort(self):
        for i in range(1, self._nItems):
            temp = self._a[i] # store the value of the element being inserted
            min = i
            while min > 0 and temp < self._a[min-1]:
                self._a[min]=self._a[min-1] #moving larger elements right until finding its spot
                min -= 1
            self._a[min]=temp



    def __str__(self):
        return str(self._a[:self._nItems])

array=Array(2)
# array.insert(1)
# array.insert(2)
# array.insert(4)
# array.insert(3)
# array.bubbleSort()
# array.insert(3)
# array.insert(4)
# array.insert(5)
# array.insert(2)
# array.insert(1)
# array.bubbleSort()
# array.selectionSort()
# #sorting_array.insertionSort()
# print(array)



class OrderedArray:
    def __init__(self,initialSize):
        self._a = [None]*initialSize
        self._nItems = 0

    def __len__(self):
        return self._nItems

    def find(self,item):
        left=0
        right=self._nItems- 1
        counter=0
        while left<=right:
            counter+=1
            mid=(left+right)//2
            if self._a[mid]==item:
                return mid
            elif self._a[mid]>item:
                right=mid-1
            else:
                left=mid+1
        print(counter)
        return -1

    def find_index(self,item):
        left=0
        right=self._nItems- 1
        while left<=right:
            mid=(left+right)//2
            if self._a[mid]==item:
                return mid
            elif self._a[mid]>item:
                right=mid-1
            else:
                left=mid+1
        return left


    def insert(self, item):
        if self._nItems >=len(self._a):
            raise Exception("Array overflow")
        j=self.find_index(item)
        for k in range(self._nItems,j,-1):
            self._a[k]=self._a[k-1]

        self._a[j]=item
        self._nItems+=1

    def delete(self,item):
        j = self.find(item)
        if j==-1:
            return False

        for k in range(j, self._nItems-1):
            self._a[k]=self._a[k+1]
            # print(self._a)

        self._a[self._nItems - 1] = None
        self._nItems -= 1
        return True

    def shuffle(self):
        for i in range(self._nItems -1, 0, -1):
            j=random.randint(0,1) # unshuffled positions
            temp = self._a[i]
            self._a[i] = self._a[j]
            self._a[j] = temp


    def __str__(self):
        return str(self._a[:self._nItems])

orderedarray=OrderedArray(20)
# orderedarray.insert(5)
# orderedarray.insert(6)
# orderedarray.insert(7)
# orderedarray.insert(8)
# orderedarray.insert(9)
# print(orderedarray.find(8))

orderedarray.insert(1)
orderedarray.insert(2)
orderedarray.insert(3)
orderedarray.insert(6)
orderedarray.insert(8)
orderedarray.insert(10)
print(orderedarray.find(17))