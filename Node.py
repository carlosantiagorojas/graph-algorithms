class Node:
    
    def __init__(self, node) -> None:
        type_result = isinstance(node, int)
        print(isinstance)
        if type_result:
            self.node = int(node)
        else:
            self.node = node

