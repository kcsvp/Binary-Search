"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        
        while len(queue)>0:
            currsize = len(queue)
            while currsize>0:
                curr = queue.popleft()
                currsize = currsize-1
                if currsize>0:
                    curr.next = queue[0]
                else:
                    curr.next= None
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root