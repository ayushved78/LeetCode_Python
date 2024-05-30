"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        node_to_clone_map = {}

        def dfs_copy(node):
            if node in node_to_clone_map:
                return node_to_clone_map[node]

            node_copy = Node(node.val)
            node_to_clone_map[node] = node_copy

            for neighbor in node.neighbors:
                neighbor_copy = dfs_copy(neighbor)
                node_copy.neighbors.append(neighbor_copy)

            return node_copy

        return dfs_copy(node)