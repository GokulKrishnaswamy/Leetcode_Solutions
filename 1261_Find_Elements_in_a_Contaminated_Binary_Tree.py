# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        # Change root val to non contaminated val
        root.val=0

        # Prepare list of values present in non contaminated tree
        self.elements = []

        #DFS
        st = [root]
        while st:
            node = st.pop()
            self.elements.append(node.val)
            
            if node.left:
                # change left node to its non contaminated value
                node.left.val = (2*node.val)+1
                st.append(node.left)
            
            if node.right:
                # change right node to its non contaminated value
                node.right.val = (2*node.val)+2
                st.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
