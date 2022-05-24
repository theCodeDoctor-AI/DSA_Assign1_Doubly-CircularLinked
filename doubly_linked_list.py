'''
    Mark Randall # 301178066
    Doubly Linked List Class
    COMP254 Sec 003
    Data Structures and Algorithms
    May 20th, 2022
'''
#%%
class Node:
    '''Class representing a Node in a DoublyLinkedList'''
    def __init__(self, data = None, next = None, prev = None):
        '''
        Constructor for the Node class
        data --> This is the element to be added to the node | None
        next --> This is the pointer to the next node in the sequence | None
        prev --> This is the pointer to the previous node in the sequence | None
        '''
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    '''Class repreenting a DoublyLinkedList'''
    def __init__(self):
        '''
        Constructor for the DoublyLinkedList (takes no arguments)
        header --> This is an empty Node to act as the header - it does not take a value
        trailer --> This is an empty Node to act as a trailer - it does not take a value

        header and trailer initialize pointing to each other (header <--> trailer). The list is still empty at this point
        '''
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, self.header)
        self.header.next = self.trailer

    def insert_at_beginning(self, data) -> None:
        '''
        Function to add a new Node at the beginning 
        data --> This is the element to be added to the Node

        Returns --> None        
        '''
        print(f'\nInserting element {data} at beginning')
        # [Header <--> Bibi <--> Mark <--> Marcus <--> Trailer]
        node = Node(data, self.header.next)
        self.header.next.prev = node
        node.prev = self.header
        self.header.next = node
        
    def insert_at_end(self, data) -> None:
        '''
        Function to add a new Node at the end
        data --> This is the element to be added to the Node

        Returns --> None
        '''
        print(f'\nInserting element {data} at end')
        node = Node(data, self.trailer)
        self.trailer.prev.next = node
        node.prev = self.trailer.prev
        self.trailer.prev = node

    def remove_first(self) -> None:
        '''Function to remove the first element'''
        print(f'\nRemoving element {self.header.next.data}')
        self.header.next.next.prev = self.header
        self.header.next = self.header.next.next

    def remove_last(self) -> None:
        '''Function to remove the last element'''
        print(f'\nRemoving element {self.trailer.prev.data}')
        self.trailer.prev.prev.next = self.trailer
        self.trailer.prev = self.trailer.prev.prev
        

    def find_node(self, data):
        '''
        Function to find a Node in the list
        data --> This is the element to be searched for

        Returns --> The Node if found else False
        '''
        current = self.header.next
        while current:
            if current.data == data:
                return current
            current = current.next
        return False

    def swap_two_nodes(self, data1, data2) -> None:
        '''
        Method to swap two the place of two Nodes by only changing connectors and not data
        data1 --> This first element in the swap
        data2 --> The second element in the swap

        Returns None        
        '''
        node1 = self.find_node(data1) 
        node2 = self.find_node(data2) 
        
        #Create temp holders for prev and next of each node to swap
        next1_temp, next2_temp, prev1_temp, prev2_temp = \
        node1.next, node2.next, node1.prev, node2.prev

        # Use the temps to reconnect to newly placed nodes
        next1_temp.prev, prev1_temp.next = node2, node2
        next2_temp.prev, prev2_temp.next = node1, node1

        # Attach the swapping nodes first
        node1.next, node1.prev, node2.next, node2.prev = \
        node2.next, node2.prev, node1.next, node1.prev

    def concat_two_lists(self, L2: 'DoublyLinkedList') -> None:
        '''
        Function to concatenate two DoublyLinkedLists (self + other)
        L2 --> Represents the list the be concatenated at the end of self

        Returns None
        '''
        last_L1_node = self.trailer.prev # grab last node before trailer of self
        first_L2_node = L2.header.next # grab the first node after header of L2 list

        # Attach
        last_L1_node.next = first_L2_node
        first_L2_node.prev = last_L1_node

    def __str__(self) -> str:
        '''
        ToString function to print contents of list
        Returns --> String representation of list elements in sequence
        '''
        if self.header.next is self.trailer:
            raise ValueError('Doubly LinkedList is empty')
        result = 'Header <--> '
        current = self.header.next
        while current:
            result += str(current.data) + ' <--> ' if current.next else 'Trailer'
            current = current.next

        return result

#%%
if __name__ == '__main__':
    dll = DoublyLinkedList()
    try:
        print(dll)
    except ValueError as e:
        print(e)
    dll.insert_at_beginning('Mark')
    print(dll)
    dll.insert_at_beginning('Bibi')
    print(dll)
    dll.insert_at_end('Marcus')
    print(dll)
    dll.insert_at_end('Megan')
    print(dll)
    
    print(f'\nSwap places of "Megan" and "Bibi" in \n[{dll}]\n')
    dll.swap_two_nodes('Megan', 'Bibi')
    print('After swap:')
    print(dll)
    print(f'\nSwap places of "Megan" and "Marcus" in \n[{dll}]\n')
    dll.swap_two_nodes('Megan', 'Marcus')
    print('After swap:')
    print(dll)
    print(f'\nSwap places of "Marcus" and "Mark" in \n[{dll}]\n')
    dll.swap_two_nodes('Marcus', 'Mark')
    print('After swap:')
    print(dll)

    dll2 = DoublyLinkedList()
    dll2.insert_at_beginning('Apple')
    dll2.insert_at_beginning('Banana')
    dll2.insert_at_beginning('Carrot')
    dll2.insert_at_beginning('Durian')
    print(dll2)
    dll.concat_two_lists(dll2)
    print(dll)


#%% Set up
# dll = DoublyLinkedList()
# try:
#     print(dll)
# except ValueError as e:
#     print(e)
# dll.insert_at_beginning('Mark')
# print(dll)
# dll.insert_at_beginning('Bibi')
# print(dll)
# dll.insert_at_end('Marcus')
# print(dll)
# dll.insert_at_end('Megan')
# print(dll)

# #%% Exercise #1
# print(f'\nSwap places of "Megan" and "Bibi" in \n[{dll}]\n')
# dll.swap_two_nodes('Megan', 'Bibi')
# print('After swap:')
# print(dll)
# print(f'\nSwap places of "Megan" and "Marcus" in \n[{dll}]\n')
# dll.swap_two_nodes('Megan', 'Marcus')
# print('After swap:')
# print(dll)

# #%% Exercise 2
# dll2 = DoublyLinkedList()
# dll2.insert_at_beginning('Apple')
# dll2.insert_at_beginning('Banana')
# dll2.insert_at_beginning('Carrot')
# dll2.insert_at_beginning('Durian')
# print(dll2)

# #%% Exercise 2 (cont)
# dll.concat_two_lists(dll2)
# print(dll)

# # %%
