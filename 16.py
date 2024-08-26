"""Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 """
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val = val
        self.children = children if children is not None else []

class Solution(object):
    def postorder(self, root):
        def traverse(node):
            if not node:
                return []
            result = []
            for child in node.children:
                result.extend(traverse(child))
            result.append(node.val)
            return result
        
        return traverse(root)

def main():
    # Example 1
    root1 = Node(1, [
        Node(3, [Node(5), Node(6)]),
        Node(2),
        Node(4)
    ])
    solution = Solution()
    print(solution.postorder(root1))  # Output: [5, 6, 3, 2, 4, 1]

    # Example 2
    root2 = Node(1, [
        Node(2),
        Node(3, [
            Node(6),
            Node(7, [
                Node(11, [Node(14)])
            ])
        ]),
        Node(4, [
            Node(8, [
                Node(12)
            ])
        ]),
        Node(5, [
            Node(9, [
                Node(13)
            ]),
            Node(10)
        ])
    ])
    print(solution.postorder(root2))  # Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]

if __name__ == "__main__":
    main()
