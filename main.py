import sys
import csv
from graph import Graph
from node import Node

def main():
    # validate_args()
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

if __name__ == '__main__':
    main()