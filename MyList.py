import ctypes 

class MyList:
    def __init__(self) -> None:
        self.size = 1
        self.n = 0 
        # create a ctype array with size = self.size
        self.A = self.__make_array(self.size) 
    
    def __len__(self) -> int:
        return self.n
    
    def append(self, item) -> None:
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)
        # append
        self.A[self.n] = item 
        self.n += 1

    def pop(self):
        # return and delete last item of list
        if(self.n == 0):
            print('Empty-List')
            return -1
        self.n = self.n - 1
        return self.A[self.n]
    
    def clear(self):
        """this method clears the all list item from list"""
        self.n = 0
        self.size = 1

    def find(self, item) -> int:
        """
        returns the index of item in the list if item is found otherwise return -1 \n
        Args: 
            item: list item
        Return: 
            int: index of item or -1
        """
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return -1
    
    def insert(self, index: int, item):
        if 0 <= index < self.n:
            # resize if list is full
            if self.n == self.size:
                self.__resize(self.size * 2)
            # shift items of (last to index+1) to make room for the item of given index
            for i in range(self.n, index, -1):
                self.A[i] = self.A[i-1]
            # insert the given items into given index
            self.A[index] = item
            self.n += 1
        else:
            print('index is out of range!')
    
    def remove(self, item):
        index = self.find(item)
        if index != -1:
            self.__delitem__(index)
        else:
            print('item is not found!')

    def __delitem__(self, index: int):
        if index < 0 or index >= self.n:
            raise IndexError('sequence index out of range')
        else:
            for i in range(index, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1

    def __str__(self) -> str:
        result = ''
        for i in range(self.n):
            if i==self.n-1:
                result = result + str(self.A[i])
            else: result = result + str(self.A[i]) + ', '
        return '['+result+']'
    
    def __getitem__(self, index) -> object:
        if 0 <= index < self.n:
            return self.A[index]
        raise IndexError('sequence index out of range')

    def __setitem__(self, index, item):
        if 0 <= index < self.n:
            self.A[index] = item
        else:
            raise IndexError('sequence index out of range')

    def __resize(self, new_capacity: int):
        # create a new araay with new capacity
        new_array = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of old array to new array
        for i in range(self.n):
            new_array[i] = self.A[i]
        # re-assign
        self.A = new_array 

    def __make_array(self, capacity):
        # creates a ctype array(static and referential) with size capacity
        return (capacity*ctypes.py_object)() 
    

arr = MyList()
arr.append('hello')
arr.append(56)
print(arr)

# print(arr[2])
# print(arr.pop())
# print(arr)
# arr.clear()
# print(arr)
# print(arr.find(45))
arr.insert(1, 'sakib')
print(arr)
# del arr[2]
# print(arr.n)
del arr[4]
arr.remove('sakib')
print(arr)

arr[3] = 67
print(arr)