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
    
    def __resize(self, new_capacity):
        # create a new araay with new capacity
        new_array = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of old array to new array
        for i in range(self.n):
            new_array[i] = self.A[i]
        # re-assign
        self.A = new_array 

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
        print('Index-Error: index out of range')

    def __make_array(self, capacity):
        # creates a ctype array(static and referential) with size capacity
        return (capacity*ctypes.py_object)() 
    

arr = MyList()
arr.append('hello')
arr.append(56)
print(arr)

print(arr[2])
print(arr.pop())
print(arr)
