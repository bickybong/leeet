# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        curr = root
        def DFS(depth, curr):
            # print(curr, depth)
            depth += 1
            if not curr:
                return depth - 1
            return max(DFS(depth, curr.left), DFS(depth, curr.right))
        return DFS(depth, curr)
        # Recursive DFS, O(n) time and O(n) space
            
        