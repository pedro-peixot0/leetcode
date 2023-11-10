from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        cloned_table = {}

        def clone_node(starting_node):
            nonlocal cloned_table
            # checking if the node is empty
            if not starting_node:
                return None

            # looking if node was already cloned
            cloned_node = cloned_table.get(starting_node.val)

            if not cloned_node:
                # creating and listing new Node
                cloned_node = Node()
                cloned_table[starting_node.val] = cloned_node

                # assigning values
                cloned_node.val = starting_node.val
                cloned_node.neighbors=[
                    clone_node(n) 
                    for n in starting_node.neighbors
                ] if starting_node.neighbors else []

            # returning node
            return cloned_node

        return clone_node(node)
