'''
good: path from root -> x has no nodes with value > value of x

given: root

return: number of good nodes


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0

        def dfs(node, max_seen):
            nonlocal good_nodes
            if not node:
                return
            
            if node.val >= max_seen:
                good_nodes += 1
                max_seen = node.val
            
            dfs(node.left, max_seen)
            dfs(node.right, max_seen)
        
        dfs(root, float("-inf"))

        
        return good_nodes

            
        