class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        
        # Like we did with linked list, we have a currentnode to traverse the tree.
        current_node = self.root
        
        while current_node != None: #we traverse while the current_node (either left or right) is not None
            if new_val < current_node: #if the new_val is less than the current_node, we should consider one case if there 
            # is anything after the current_node and another case if there's already something after the current_node
                if current_node.left == None: # if there is nothing:
                    current_node.left = Node(new_val) # I create a new Node
                    break #operation finished -> avoid infinite loop and exit the while loop.
                current_node = current_node.left
                 
            else: 
                if current_node.right == None:
                    current_node.right = Node(new_val)
                    break
                current_node = current_node.right #if there is already something on the right
       

    def search(self, find_val):
        # We benefit as the array is sorted, we don't need to use recursion. 
        # This way to code is smart because I adapt the current_node to be a new node after I checked if the value is < > to the current node.
        current_node = self.root
        
        while current_node != None: 
            if current_node.value == find_val:
                return True
            elif find_val < current_node:
            # we change the currentnode after we checked if the number is < or >
                current_node = current_node.left
            else:
                current_node = current_node.right
   
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
