import sys
import csv
from Node import Node


def main():
    validate_args()
    Node('s')
    # graph = Graph()
    # graph.add_node('s')
    # graph.add_node('t')
    # graph.add_node('y')
    # graph.add_edge('s', 't', 10)
    # graph.add_edge('s','y', 5)
    # graph.print_graph()
    # #validate_args()    

def validate_args():
    arguments = len(sys.argv[1:])
    if arguments == 1:
        crate_graph_csv(sys.argv[1])
    elif arguments < 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def crate_graph_csv(file_name: str):
    graph = Graph()
    if file_name.endswith(".csv"):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                for i, value in enumerate(row):
                    if i == 0:
                        pass
                        

class Graph:

    def __init__(self, directed = True) -> None:
        """Initialize the graph with and adjancency list like a dictionary and like a directed or undirected graph

        Args:
            directed (bool, optional): Initialize the graph as directed or undirected. Defaults to True.
        """
        self.adj_list = {}
        self.graphtype = directed

    def add_node(self, node) -> bool:
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
    
    def add_edge(self, origin_node, destination_node, weight) -> bool:
        """Add an edge from the origin node to the destination node

        Args:
            origin_node (_type_): _description_
            destination_node (_type_): _description_
            weight (_type_): _description_

        Returns:
            bool: _description_
        """
        # check if the origin node and destinaiton node are in the adjacency list
        if origin_node not in self.adj_list:
            print(f"the origin node: {origin_node} does not exist")
            return False
        if destination_node not in self.adj_list:
            print(f"the destination node: {destination_node} does not exist")
            return False
        
        # add the edge like a tuple
        self.adj_list[origin_node].append((destination_node, weight))
        
        # if the graph is not directed add the other edge
        if not self.graphtype:
            self.adj_list[destination_node].add((origin_node, weight))
                
        return True
    
    def print_graph(self):
        """Print a the graph, shows the nodes next to the edges
        """
        for key in self.adj_list.keys():
            print(key, ": ", self.adj_list[key])

if __name__ == '__main__':
    main()