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
            origin_node (Node): Origin node of the edge
            destination_node (Node): Destination node of the edge
            weight (any): Weight of the edge

        Returns:
            bool: True if the add can be created, False if not
        """
        # print(ori_node, dest_node, weight)
        weight = self.convert_weight(weight)
        
        # check if the origin node and destinaiton node are in the adjacency list
        if ori_node not in self.adj_list.keys():
            print(f"the origin node: {ori_node} does not exist")
            return False
        if dest_node not in self.adj_list.keys():
            print(f"the destination node: {dest_node} does not exist")
            return False
        
        # add the edge like a tuple
        self.adj_list[ori_node].append((dest_node, weight))
        
        # if the graph is not directed add the other edge
        if not self.graphtype:
            self.adj_list[dest_node].add((ori_node, weight))
                
        return True
    
    def convert_weight(self, weight):
        """Convert the weight to his corresponding type

        Args:
            weight (any): Value that represents the weight

        Returns:
            any: Returns the weight like and int or str
        """
        if isinstance(weight, (int, float)):
            return weight
        try:
            # Attempt to convert to int
            return int(weight)
        except ValueError:
            try:
                # Attempt to convert to float
                return float(weight)
            except ValueError:
                # If conversion to int or float fails, return a default value or handle it as needed
                return 0  # You can change this default value to something appropriate
    
    def search_node_value_key(self, value) -> Node:
        """Search if a node exists with the value, return the searched node (key in the dictionary)

        Args:
            value (any): A value that represents the node

        Returns:
            Node: The searched node if finded, if not return None
        """
        for key in self.adj_list.keys():
            if key.value == value:
                return key
        return None
    
    def search_node_value(self, value) -> int:
        """Search if a node exists with the value, return the index of the searched node

        Args:
            value (any): A value that represents the node

        Returns:
            Node: The index searched node if finded, if not return None
        """
        for i, key in enumerate(self.adj_list.keys()):
            if key.value == value:
                return i
        return None
    
    def search_node_index(self, index) -> Node:
        """Search if a node exists with the index, return the searched node

        Args:
            value (any): A index

        Returns:
            Node: The searched node if finded, if not return None
        """
        for i, key in enumerate(self.adj_list.keys()):
            if i == index:
                return key
        return None
    
    def search_node(self, node: Node) -> int:
        """Search the position of a node in the dict, return the index of the searched node

        Args:
            value (any): A value that represents the node

        Returns:
            Node: The index searched node if finded, if not return None
        """
        for i, key in enumerate(self.adj_list.keys()):
            if key == node:
                return i
        return None
        
    def node_exists(self, node: Node) -> bool:
        return node in self.adj_list.keys()
        
    def print_graph(self):
        """Print a the graph, shows the nodes next to the edges
        """
        for key in self.adj_list.keys():
            print(key, ": [",end='')
            for node, weight in self.adj_list[key]:
                print(f"({node}, {weight})",end="")
            print("]")
    
    def number_of_nodes(self) -> int:
        """Know the number of nodes in the graph

        Returns:
            int: Number of keys (nodes) in the dictionary
        """
        return len(self.adj_list.keys())
    
    def get_all_nodes(self) -> list:
        """Get all the nodes of the graph as a list

        Returns:
            list: All the nodes in the graph
        """
        all_nodes = []
        for key in self.adj_list.keys():
            all_nodes.append(key)
        return all_nodes
    
    def print_all_elements_tab(self, list: list):
        """Print the elements of a list

        Args:
            list (list): List of elements
        """
        for element in list:
            print(element, end="\t")
        print()
    
    def print_all_elements(self, list: list):
        print("[", end=" ")
        for element in list:
            print(element, end=" ")
        print("]")
        
    def bfs(self, source: int) -> list:
        """BFS implementation with a queue

        Args:
            source (int): The index of the source node

        Returns:
            list: List of the visited nodes in order
        """
        
        # Create a queue and add the source node to start the search
        queue = []
        queue.append(self.search_node_index(source))
        # Create a list of visited nodes
        visited = []
        current_node = None
        
        # iter = 1
        
        while len(queue) != 0:
            # print("\nIter " , iter)
            # See the first element of the queue 
            current_node = queue.pop(0)
            # print(f"Current node: {current_node}")
            # If the current node is not in the visited list
            if current_node not in visited:
                visited.append(current_node)
                # Iterate over the neighbours of the current node and add them to the queue
                for node, weight in self.adj_list[current_node]:
                    # print(f"Neighbour node: {node}")
                    queue.append(node)
            # iter += 1
        
        print("\nBFS...")
        self.print_all_elements(visited)
        
        return queue
    
    def dfs(self, source: int) -> list:
         
        # Create a stack and add the source node to start the search
        stack = []
        stack.append(self.search_node_index(source))
        # Create a list of visited nodes
        visited = []
        current_node = None
        
        while len(stack) != 0:
            current_node = stack.pop()
            if current_node not in visited:
                visited.append(current_node)
                for node, weight in self.adj_list[current_node]:
                    # print(f"Neighbour node: {node}")
                    stack.append(node)
       
        print("\nDFS...")
        self.print_all_elements(visited)    
    
    def dijkstra(self, source: int) -> list:
        """Dijkstra algorithm

        Args:
            source (int): Index of the source node

        Returns:
            list: Minimum istance to all the other nodes
        """
        
        print("\nDijkstra algorithm...")
        
        number_nodes = self.number_of_nodes()
        
        # Create a list of distances set to infinty with the same size as the number of nodes
        dist = [float('inf')] * number_nodes
        dist[source] = 0 # Set the distance to the source node to 0
        
        # Create a list fo predecesors with the same size as the number of nodes
        pred = [None] * number_nodes
        pred[source] = self.search_node_index(source) # Set the predecesor of the source node as itself
        
        # Set a list of all the nodes to control when the algorithm has to finish
        nodes_queue = self.get_all_nodes()
        nodes = self.get_all_nodes()
        
        # Set a list of visited nodes
        visited = []
        current_node = None
        current_index = None
        pop_index = None
        iter = 1
        
        while len(nodes_queue) != 0:
            print(f"\nIteration: {iter}")
            self.print_dijkstra(nodes, dist, pred, visited, nodes_queue)
            
            # Select the node with the minimum distance
            min_dist = float('inf')
            for i in range(len(nodes_queue)):
                if nodes_queue[i] not in visited:
                    print(f"not visited: {nodes_queue[i]}")
                    distance = dist[self.search_node(nodes_queue[i])]
                    if distance < min_dist:
                        current_node = nodes_queue[i]
                        min_dist = distance
                        current_index = self.search_node(current_node)
            
            print(f"current: {current_node}", f" index: {self.search_node(current_node)}")
            visited.append(current_node)
            
            # Look for the neighbours of the current node
            for neighbour, weight in self.adj_list[current_node]:
                print(f"neighbour: {neighbour}", f"weight: {weight}")
                neighbour_index = self.search_node(neighbour)
                # If the distance of the neighbour is higher than the current distance of the node plus the weight
                if dist[neighbour_index] > dist[current_index] + weight:
                   dist[neighbour_index] = dist[current_index] + weight # Set the new current distance
                   pred[neighbour_index] = current_node # Set the new predecesor
            
            # Look for the index of the current node in the queue
            for i in range(len(nodes_queue)):
                if nodes_queue[i] == current_node:
                    pop_index = i

            # Remove the current node from the queue
            nodes_queue.pop(pop_index)
            iter += 1
        
        print(f"\nResult:")
        self.print_dijkstra(nodes, dist, pred, visited, nodes_queue)
        
        return dist
        
    def print_dijkstra(self, nodes: list, dist: list, pred: list, visited: list, nodes_queue: list):
        print("\t", end=" ")
        self.print_all_elements_tab(nodes)
        print("distance", end=" ")
        self.print_all_elements_tab(dist)
        print("predeces", end=" ")
        self.print_all_elements_tab(pred)
        print("visited ", end=" ")
        self.print_all_elements_tab(visited)
        print("queue   ", end=" ")
        self.print_all_elements_tab(nodes_queue)
        print("\n")