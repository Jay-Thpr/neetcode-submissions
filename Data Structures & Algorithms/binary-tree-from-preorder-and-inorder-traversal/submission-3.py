# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''

process 1 node at a time in preorder
if node is on the left: will be on the left in inorder
if node is on the right: will be on the right in inorder

'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        n = len(preorder)

        indices = {}

        for i in range(len(inorder)):
            indices[inorder[i]] = i
        
        i = 0

        def build(left, right):
            nonlocal i
            if left > right:
                return None

            val = preorder[i]
            node = TreeNode(val)
            i += 1

            mid = indices[val]
            
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node
        return build(0, n - 1)
            






        