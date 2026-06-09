# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return None
            else:
                temp1=dfs(root.left)
                temp2=dfs(root.right)
                root.right=temp1
                root.left=temp2
                return root
        return(dfs(root))
        