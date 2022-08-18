"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Possible Solutions: 
1) Recursion based
counter loop for each section of subtrees visited (starting at 1 bc of root level is included)
return max(counter)

-two counters needed for both initial sides of root? and max(l_counter, r_counter) # prob not!
- not even counter required to be inserted as an argument, can initialize counter = 1 
- return max(rec(left_tree, l_counter), rec(right_tree, r_counter))


-pass in updated counters to each function call?

Edgecases{
    1) if not (root.left or root.right):
        return 1
    2) if root is null:
        return 0
}
Pseudocode:
1)
l_counter  = r_counter = 1
 - while(root.left or root.right):
    counter ++
    if(root.left):
        method(root.left)
    if(root.right):
        method(root.right)

return max(counter)

CORRECT SOLUTION: much simpler :(((
    
def depth(node, count):
            if node:
				# depth + 1 because node is not null
                count += 1 
                # max depth of the left child node
                lcount = depth(node.left, count)
                # max depth of the right child node
                rcount = depth(node.right, count)
                return max(lcount, rcount)
            else:
                return count
        
        #
        return depth(root, 0)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if not (root.left or root.right):
            return 1
        
        def depth(node, count):
            if node:
                #depth + 1 bc node != None
                count += 1
                #max depth of left child node
                lcount = depth(node.left, count)
                #max depth of right child node
                rcount = depth(node.right, count)
                return max(lcount, rcount)
            else:
                return count
          
        return depth(root, 0)

        #optimized solution:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        #explores left and right children's depths
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        #returns max depth between left and right children and adds 1 because it is the parent itself
        return max(left, right) + 1
    