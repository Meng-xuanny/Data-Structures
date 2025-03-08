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
            # swapped = False  # Track if a swap happens
            for k in range(j):
                innnerIteration+=1
                if self._a[k]>self._a[k+1]:
                    temp = self._a[k]
                    self._a[k]=self._a[k+1]
                    self._a[k + 1]=temp
            #         swapped = True
            # if not swapped:
            #     break  # Stop early if no swaps

        print(outIteration, innnerIteration)

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

        print(outIteration, innnerIteration)


    def insertionSort(self):
        for i in range(1, self._nItems):
            temp = self._a[i] # store the value of the element being inserted
            min = i
            while min > 0 and temp < self._a[min-1]:
                self._a[min]=self._a[min-1] #moving larger elements right until finding its spot
                min -= 1
            self._a[min]=temp

    def shellSort(self):
        h=1
        while h<= self._nItems//3:
            h=h*3 +1
        while h > 0:
            for outer in range(h, self._nItems): # we consider elements that are at least h positions apart.
                temp=self._a[outer]
                inner = outer
                while inner> h-1 and temp < self._a[inner-h]:
                    self._a[inner]=self._a[inner-h]
                    inner-=h
                self._a[inner]=temp
            h=(h-1)//3 #Reduce the Gap, repeats until h = 1, at which point it behaves like a normal Insertion Sort.

    # def partition(self, lo, hi, key):
    #     pivot = key(self._a[hi])  # Correct pivot selection
    #     left, right = lo, hi -1  # `right` starts before pivot, if pointing at the pivot,right pointer won't move backwards
    #
    #     while left <= right: #swap pairs
    #         while left <= right and key(self._a[left]) < pivot:
    #             left += 1
    #         while left <= right and key(self._a[right]) > pivot:
    #             right -= 1
    #         if left <= right:
    #             self._a[left], self._a[right] = self._a[right], self._a[left]  # Swap
    #             left += 1
    #             right -= 1
    #
    #     # Move pivot to correct position
    #     self._a[left], self._a[hi] = self._a[hi], self._a[left]
    #     return left  # New pivot index

    def median_of_three(self, lo, hi):
        """Find the median of first, middle, and last elements."""
        mid = (lo + hi) // 2
        a, b, c = self._a[lo], self._a[mid], self._a[hi]

        # Find the median value among a, b, c and return its index
        if (a < b < c) or (c < b < a):
            return mid  # b is the median
        elif (b < a < c) or (c < a < b):
            return lo  # a is the median
        else:
            return hi  # c is the median

    def partition(self, lo, hi, key=lambda x: x):
        # Find the median-of-three pivot index
        pivot_index = self.median_of_three(lo, hi)
        self._a[pivot_index], self._a[hi] = self._a[hi], self._a[pivot_index] # Swap pivot to end

        #normal last element as pivot
        pivot = key(self._a[hi])  # Choose the last element as the pivot
        i = lo -1  # Pointer for the smaller element

        for j in range(lo, hi):  # Loop through elements
            if key(self._a[j]) <= pivot:  # If element is smaller than pivot
                i += 1
                self._a[i], self._a[j] = self._a[j], self._a[i]  # swap with the first bigger element

        # Swap pivot into correct position
        self._a[i + 1], self._a[hi] = self._a[hi], self._a[i + 1]
        return i + 1  # Return pivot index

    def quicksort(self, lo=0, hi=None, key=lambda x: x):
        if hi is None:
            hi = self._nItems - 1
        if lo >= hi:
            return

        p = self.partition(lo, hi, key)  # Partition the array
        print(self._a)
        self.quicksort(lo, p - 1, key)  # Sort left partition, pivot is already at correct place
        self.quicksort(p + 1, hi, key)  # Sort right partition

    def __str__(self):
        return str(self._a[:self._nItems])

array=Array(2)
# array.insert(1)
# array.insert(2)
# array.insert(4)
# array.insert(3)
# print(array)
# array.bubbleSort()
array.insert(3)
array.insert(4)
array.insert(5)
array.insert(2)
array.insert(1)
# array.bubbleSort()
# array.selectionSort()
# #sorting_array.insertionSort()
# array.shellSort()
array.quicksort()
print(array)



class OrderedArray:
    def __init__(self,initialSize):
        self._a = [None]*initialSize
        self._nItems = 0

    def __len__(self):
        return self._nItems

    def find(self, item):
        left = 0
        right = self._nItems - 1
        counter = 0
        while left <= right:
            mid = (left + right) // 2
            counter += 1
            if self._a[mid] == item:
                print(counter)  #iterations it takes to find the item
                return mid
            elif self._a[mid] > item:
                right = mid - 1
            else:
                left = mid + 1

        print(counter) #iterations it takes to end the loop
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
            j=random.randint(0,i) # unshuffled positions
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
# print(orderedarray)
# print(orderedarray.find(8))

orderedarray.insert(1)
orderedarray.insert(2)
orderedarray.insert(3)
orderedarray.insert(6)
orderedarray.insert(8)
orderedarray.insert(10)
print(orderedarray.find(17))