class Node:
    
    def __init__(self, value) -> None:
        if isinstance(value, int):
            self.value = int(value)
        else:
            self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

