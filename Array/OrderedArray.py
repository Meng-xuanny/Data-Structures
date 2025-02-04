class Array():
    def __init__(self,initialSize):
        self._a=[None] * initialSize
        self._nItems=0

    def __len__(self):
        return self._nItems

    def insert(self,item):
        if self._nItems >= len(self._a):
            raise Exception("Array overflow")
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

    def __str__(self):
        return str(self._a[:self._nItems])

array=Array(3)
array.insert("a")
array.insert("b")
array.insert("c")
# print(array.find("c"))
array.delete("b")
# array.delete("b")
# array.delete("a")
print(array)



class OrderedArray:
    def __init__(self,initialSize):
        self._a = [None]*initialSize
        self._nItems = 0

    def __len__(self):
        return self._nItems

    def find(self,item):
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
        for k in range(self._nItems, j, -1):
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



    def __str__(self):
        return str(self._a[:self._nItems])

orderedarray=OrderedArray(5)
orderedarray.insert(1)
orderedarray.insert(3)
orderedarray.insert(7)
orderedarray.insert(5)
orderedarray.insert(4)
print(orderedarray)
print(orderedarray.find(3))
orderedarray.delete(7)
print(orderedarray)