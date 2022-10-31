class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val)
                   and valid(node.right, node.val, right))
        
        return valid(root, float('-inf'), float('inf'))

sol = Solution()
print(sol.isValidBST( [5,4,6,None,None,3,7]))