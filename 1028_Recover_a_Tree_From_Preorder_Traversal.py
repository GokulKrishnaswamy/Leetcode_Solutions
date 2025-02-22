# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        # Find all values and its depth in tree
        values, depth = [], []
        i=0
        while i<len(traversal):
            d = 0
            while traversal[i] == "-":
                d+=1
                i+=1
            val = ""
            while i<len(traversal) and traversal[i] != "-":
                val = val+traversal[i]
                i+=1
            values.append(int(val))
            depth.append(d)

        
        def get_node(tree_values:list, tree_depth:list) -> TreeNode:
            # if no subtree present, return None
            if len(tree_depth)==0:
                return None
        
            # create current node - first value in the list because of pre order traversal
            current_depth = tree_depth[0]
            node_val = tree_values[0]
            node = TreeNode(int(node_val))

            #calculate next_depth to recurse
            next_depth = current_depth + 1
            
            # find indices in the list where next depth occurs
            inds = [i for i in range(0,len(tree_depth)) if tree_depth[i]==next_depth]

            # case 1: no subtree present
            left_values, left_depths = [], []
            right_values, right_depths = [], []

            # case 2:  only left subtree is present
            if len(inds)==1:
                left_values, left_depths = tree_values[1:], tree_depth[1:]
            
            # case 3: left and right subtree present
            if len(inds)==2:
                ind = inds[-1]
                left_values, left_depths = tree_values[1:ind], tree_depth[1:ind]
                right_values, right_depths = tree_values[ind:], tree_depth[ind:]

            #recursion!
            node.left = get_node(left_values, left_depths)
            node.right = get_node(right_values, right_depths)

            #return the current node
            return node
        
        return get_node(values, depth)

