class Node:
    '''
    A Node class
    '''
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        '''
        Link to the first element
        '''
        self.head = None

    def append(self, value):
        '''
        Append a value to LinkedList
        O(N)
        '''
        # Set value as head if LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # Find Node without next_node
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        
        # Set value as next_node for current Node
        current.next_node = Node(value)
    
    def __str__(self):
        '''
        Return all elements as a string
        '''
        current = self.head
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"