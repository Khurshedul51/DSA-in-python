class Node:
    def __init__(self, value, next_node=None) -> None:
        self._data = value
        self._next = next_node

class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__no_of_nodes = 0
    
    def __len__(self) -> int:
        return self.__no_of_nodes
    
    def __str__(self) -> str:
        linked_list_str = ''
        head_node = self.__head
        if head_node != None:
            current_node = head_node
            while current_node != None:
                arrow = ' -> ' if current_node._next != None else ''
                linked_list_str = linked_list_str + str(current_node._data) + arrow
                current_node = current_node._next
            return f'[{linked_list_str}]'
        else:
            return '[]'

    
    def insert_head(self, value):
        # new node
        new_node = Node(value, next_node=self.__head)
        # reassign head and tail
        if self.__tail == None:
            self.__tail = new_node
        self.__head = new_node
        # increment length of linked list by 1
        self.__no_of_nodes += 1
    
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail._next = new_node
            self.__tail = new_node
        self.__no_of_nodes += 1

    def insert_after(self, after, value):
        searched_node = self.search_node_by_value(after)
        if searched_node != None:
            if searched_node._next == None:
                self.append(value)
            else:
                next_of_searched_node = searched_node._next
                searched_node._next = Node(value, next_node=next_of_searched_node)
                self.__no_of_nodes += 1
        else:
            raise ValueError('value of [arg: after] is not found')

    def search_node_by_value(self, value) -> Node | None:
        current_node = self.__head
        while current_node != None:
            if current_node._data == value:
                return current_node
            current_node = current_node._next
        return None
    
    def remove(self, value):
        pass

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__no_of_nodes = 0
    
    def delete_head(self):
        if not self.is_empty():
            self.__head = self.__head._next
            self.__no_of_nodes -= 1
    
    def delete_tail(self):
        """deletes the nodes from the last"""
        if not self.is_empty():
            current_node = self.__head
            if current_node._next != None:
                second_last_node = None
                while current_node._next._next != None:
                    current_node = current_node._next
                current_node._next = None
                self.__tail = current_node
            else:
                self.__head = None
                self.__tail = None
            self.__no_of_nodes -= 1


    def get_last_value(self):
        return self.__tail._data
    def get_last_node(self):
        return self.__tail
    
    def get_first_value(self):
        return self.__head._data
    def get_first_node(self):
        return self.__head
    
    def is_empty(self):
        return True if self.__head == None else False
    
# ------------------------------------------------------------------------ #

linked_list = LinkedList()
# linked_list.insert_head(45)
# linked_list.insert_head(67)
# linked_list.insert_head(90)
# print(linked_list.get_last_value())
linked_list.append(12)
linked_list.append('sakib')
# linked_list.append('didar')
linked_list.insert_after(12, 'rakib')
# linked_list.insert_after('sakib', 89)

print(len(linked_list))
print(linked_list)
# print(linked_list.get_first_value())
print(linked_list.is_empty())
# linked_list.delete_head()
# linked_list.delete_head()
# linked_list.delete_head()
linked_list.delete_tail()
linked_list.delete_tail()
linked_list.delete_tail()
print(linked_list)
print(len(linked_list))
# print(linked_list.search_node_by_value('sakib'))