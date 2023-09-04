import sys
import csv
import os
from graph import Graph
from node import Node


def main():
    file_name = validate_args()
    graph = create_graph_csv(file_name)
    graph.print_graph()  
    menu(graph)
    
def validate_args() -> str:
    """Validate the arguments of execution

    Returns:
        str: The argument with the file name of the CSV
    """
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
    """Create the graph with a CSV file

    Args:
        file_name (str): Name of the CSV file

    Returns:
        Graph: The created graph
    """
    new_graph = Graph(True)
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Create the variables
            ori_node = None
            dest_node = None
            weight = None
            for i, value in enumerate(row):
                # First column (origin node)
                if i == 0:
                    ori_node = new_graph.search_node_value(value)
                    if ori_node == None:
                        ori_node = Node(value)
                        new_graph.add_node(ori_node)
                # Second column (destination node)
                elif i == 1: 
                    dest_node = new_graph.search_node_value(value)
                    if dest_node == None:
                        dest_node = Node(value)
                        new_graph.add_node(dest_node)
                # Third column (weight)                        
                elif i == 2:
                    weight = value
                    # Create the edge
                    new_graph.add_edge(ori_node, dest_node, weight)
    return new_graph
                    
def menu(graph: Graph):
    option = None
    while option != 0:
        print("\nType the number of the algorithm to execute: ")
        print("1. Dijkstra")
        print("2. Ford-fulkerson")
        print("3. Prim")
        print("4. Kosaraju")
        print("0 to exit...\n")
        
        option = input("Type: ")
        valid_input = False
        
        try:
            option = int(option)
            valid_input = True
        except ValueError:
            print("Invalid input")

        if valid_input:
            if option == 0:
                sys.exit
            elif option in range(1,4):
                os.system("cls")
                match option:
                    case 1:
                        graph.dijkstra()
            else:
                print("The number is not in the range of the options")        

                         
if __name__ == '__main__':
    main()