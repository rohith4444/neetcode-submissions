# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root, target):
            if not root:
                return None
            if root == target:
                return [root]
            
            left = findPath(root.left, target)
            if left:
                return [root] + left
            
            right = findPath(root.right, target)
            if right:
                return [root] + right
            
            return None

        pPath = findPath(root, p)
        qPath = findPath(root, q)

        # Compare paths, find last common node
        result = root
        for i in range(min(len(pPath), len(qPath))):
            if pPath[i] == qPath[i]:
                result = pPath[i]
            else:
                break

        return result

