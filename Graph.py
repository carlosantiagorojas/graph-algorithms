from node import Node

class Graph:

    def __init__(self, directed = True) -> None:
        """Initialize the graph with and adjancency list like a dictionary and like a directed or undirected graph

        Args:
            directed (bool, optional): Initialize the graph as directed or undirected. Defaults to True.
        """
        self.adj_list = {}
        self.graphtype = directed

    def add_node(self, node: Node) -> bool:
        """Add the node to the graph

        Args:
            node (): the node to be added to the graph

        Returns:
            bool: True if the node was added, False otherwise
        """
        try:
            self.adj_list[node] = []
            return True
        except Exception:
            print("Cannot add the node")
            return False
    
    def add_edge(self, ori_node: Node, dest_node: Node, weight) -> bool:
        """Add an edge from the origin node to the destination node

        Args:
            origin_node (_type_): _description_
            destination_node (_type_): _description_
            weight (_type_): _description_

        Returns:
            bool: _description_
        """
        
        weight = self.convert_weight(weight)
        
        # check if the origin node and destinaiton node are in the adjacency list
        if ori_node not in self.adj_list:
            print(f"the origin node: {ori_node} does not exist")
            return False
        if dest_node not in self.adj_list:
            print(f"the destination node: {dest_node} does not exist")
            return False
        
        # add the edge like a tuple
        self.adj_list[ori_node].append((dest_node, weight))
        
        # if the graph is not directed add the other edge
        if not self.graphtype:
            self.adj_list[dest_node].add((ori_node, weight))
                
        return True
    
    def print_graph(self):
        """Print a the graph, shows the nodes next to the edges
        """
        for key in self.adj_list.keys():
            print(key, ": ", self.adj_list[key])
            
    def convert_weight(self, weight):
        if isinstance(weight, int):
            return int(weight)
        else:
            return weight