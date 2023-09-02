import sys
import csv
from graph import Graph
from node import Node

def main():
    file_name = validate_args()
    graph = create_graph_csv(file_name)
    graph.print_graph()
    # graph = Graph()
    # first_node = Node('s')
    # graph.add_node(first_node)
    # graph.print_graph()
    # exist = graph.search_node(first_node)
    # print(exist)
    # graph.add_node('t')
    # graph.add_node('y')
    # graph.add_edge('s', 't', 10)
    # graph.add_edge('s','y', 5)
    # graph.print_graph()
    # #validate_args()    

def validate_args() -> str:
    arguments = len(sys.argv[1:])
    if arguments == 1:
        if sys.argv[1].endswith(".csv"):
            return sys.argv[1]
        else:
            sys.exit("Invalid input file")
    elif arguments < 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def create_graph_csv(file_name: str) -> Graph:
    new_graph = Graph(True)
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ori_node = None
            dest_node = None
            weight = None
            for i, value in enumerate(row):
                if i == 0:
                    ori_node = new_graph.search_node_value(value)
                    if ori_node == None:
                        ori_node = Node(value)
                        new_graph.add_node(ori_node)
                elif i == 1: 
                    dest_node = new_graph.search_node_value(value)
                    if dest_node == None:
                        dest_node = Node(value)
                        new_graph.add_node(dest_node)
                elif i == 2:
                    weight = value
                    new_graph.add_edge(ori_node, dest_node, weight)
    return new_graph
                    
                    

if __name__ == '__main__':
    main()