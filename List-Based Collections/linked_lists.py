"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        current_node = self.head
        counter = 1
        
        if position < 1:
            return None
        while current_node != None:
            if counter == position:
                return current_node
            current_node = current_node.next
            counter += 1
        
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        current_node = self.head
        counter = 1
        temp_node = None
        
        if position == 1:
            new_element.next = self.head
        else:
            while counter <= position:
                if counter == position-1:
                    temp_node =  current_node.next
                    current_node.next = new_element
                    new_element.next = temp_node
                counter += 1
                current_node = current_node.next
            
    def delete(self, value):
        "Delete the value in the linked list"
        current_node = self.head
        
        if self.head.value == value:
            self.head = self.head.next
        
        while current_node.next != None:
            if current_node.next == value:
                current_node.next = current_node.next.next
            current_node = current_node.next
            
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value
# Test insert
ll.insert(e4,3) # 1 - 2 - 4 - 3 
print("List", ll.head.next.next.next.value)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
print("List", ll.head.value)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
