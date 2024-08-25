# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(node):
            if node is None:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]

        return postorder(root)

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root))  # Output: [3, 2, 1]