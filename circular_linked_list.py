'''
    Mark Randall # 301178066
    Doubly Linked List Class
    COMP254 Sec 003
    Data Structures and Algorithms
    May 20th, 2022
'''

#%%
class Node:
    '''
    Class representing a node in a sequence
    
    data --> This is the element to be stored in the node

    '''
    def __init__(self, data):
        '''Constuctor for the Node - next is defaulted to None'''
        self.data = data
        self.next = None

class CircularLinkedList:
    '''Class representing a Circular Linkeded List'''
    def __init__(self):
        '''Constructor for Circular Linked List - head is defaulted to None'''
        self.head = None

    def add_data(self, data) -> None:
        '''
        Function to add a new Node to the list

        data --> This is the element to be added in the new Node

        Returns --> None
        '''
        node = Node(data)
        temp = self.head
        node.next = self.head

        if self.head is not None:  # the list is not empty
            while(temp.next != self.head): # loop to walk through the list comparing temp to the head
                temp = temp.next
            temp.next = node # the next node was head so we can place new node here
        else:
            node.next = node # the above block fails since the list is too small to run the loop
        self.head = node # the list was empty and the new node is the head


    def contains(self, data):
        '''
        Function to parse list and determine if it contains provided element
    
        data --> This is the element to be added to the list

        Returns --> Node if found else False
        '''
        if self.head.data == data: # check for a quick response before traversing
            return self.head
        else:
            temp = self.head
            if self.head is not None: # the list is not empty
                while(True): # traverse
                    temp = temp.next
                    if (temp.data == data): # check data at each iteration
                        return temp # found return the Node
                    if temp == self.head:
                        break
        return False # element not found


    def __eq__(self, other: 'CircularLinkedList') -> bool:
        '''
        Overload method for the == operator to compare equality based on data points stored within the Nodes in each list and their respective sequence.

        other --> This represents the CircularLinkedList to compare to the first

        Returns --> True if elements in sequence match else False

        Raises ValueError if argument 'other' is not of type CircularLinkedList
        '''
        if not isinstance(other, CircularLinkedList):
            raise ValueError('Argument supplied must be a CircularLinkedList')

        temp = self.head

        match = self.head if self.head.data == other.head.data else None

        if not match:
            match = other.contains(self.head.data)
            if not match:
                return False
            else:
                other.head = match

        other_temp = other.head.next
        
        temp = temp.next

        while(True):
            if temp == self.head:
                break
            elif temp.data == other_temp.data:
                temp = temp.next
                other_temp = other_temp.next            
            else:
                return False
        return True

                
    def __str__(self) -> str:
        '''ToString function to print the contents of the list'''
        temp = self.head
        result = ''
        if self.head is not None:
            while(True):
                result += str(temp.data + ' --> ')
                temp = temp.next
                if temp == self.head:
                    break
        return result          
#%%


if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.add_data('Mark')
    cll.add_data('Bibi')
    cll.add_data('Marcus')
    cll.add_data('Megan')
    print(cll)

    cll2 = CircularLinkedList()
    cll2.add_data('Mark')
    cll2.add_data('Bibi')
    cll2.add_data('Marcus')
    cll2.add_data('Megan')
    print(cll2)

    cll3 = CircularLinkedList()
    cll3.add_data('Apple')
    cll3.add_data('Banana')
    cll3.add_data('Carrot')
    cll3.add_data('Durian')
    print(cll3)

    print(f' is [{cll}] == to [{cll2}]?')
    print(cll == cll2)
    print(f' is [{cll}] == to [{cll3}]?')
    print(cll == cll3)


# #%%
# cll = CircularLinkedList()
# cll.add_data('Mark')
# cll.add_data('Bibi')
# cll.add_data('Marcus')
# cll.add_data('Megan')
# print(cll)

# # %%
# cll2 = CircularLinkedList()
# cll2.add_data('Mark')
# cll2.add_data('Bibi')
# cll2.add_data('Marcus')
# cll2.add_data('Megan')
# print(cll2)

# # %%
# cll3 = CircularLinkedList()
# cll3.add_data('Apple')
# cll3.add_data('Banana')
# cll3.add_data('Carrot')
# cll3.add_data('Durian')
# print(cll3)

# #%%
# print(f' is [{cll}] == to [{cll2}]?')
# print(cll == cll2)
# print(f' is [{cll}] == to [{cll3}]?')
# print(cll == cll3)
# # %%
