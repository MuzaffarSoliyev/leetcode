# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.is_mirror(root.left, root.right)

    def is_mirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and self.is_mirror(leftroot.left, rightroot.right) and self.is_mirror(
                leftroot.right, rightroot.left)
        return leftroot == rightroot
