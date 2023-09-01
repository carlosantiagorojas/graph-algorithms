class Node:
    
    def __init__(self, node) -> None:
        if isinstance(node, int):
            self.node = int(node)
        else:
            self.node = node

