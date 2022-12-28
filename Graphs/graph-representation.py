class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found) #creating the edge between the from node and the to node.
        from_found.edges.append(new_edge) #from_found can have access to all the variables in the init.
        #from_found is a node, and it has a edges variable line4
        # append the new edge to the from_found node
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edges = []
        for edge in self.edges:
            edges.append((edge.value, edge.node_from.value, edge.node_to.value))
            #we created a tuple because they said 'triplets' so we guess they meants triplets.
        return edges

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        # a range from 0 up to the maximum node value
        adj_list = []
        idx =0
        while idx <= len(self.nodes):
            temp = []
            
            for edge in self.edges:
                if idx == edge.node_from.value:
                    temp.append((edge.node_to.value, edge.value))
            
            if temp == []:
                adj_list.append(None)
            else:
                adj_list.append(temp)
            
            idx += 1
        
        return adj_list
                    
            
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
        # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
        
        idx_from = 0
        adj_matrix = []
        while idx_from <= len(self.nodes):
            idx_to = 0 
            temp = []
            while idx_to <= len(self.nodes):
                temp.append(0) 
                idx_to += 1
            
            adj_matrix.append(temp)
            
            idx_from += 1
        
        for edge in self.edges:
            adj_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        
        return adj_matrix    
       
       

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

#print(len(graph.nodes))

# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print graph.get_edge_list()
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()
