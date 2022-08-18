"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Possible Solution:
Recursion based,  checking symmetry based on boolean value of whether nodes are present on both sides ( and in the accurate position).
 -if nodes present and are in correct placement, check node.val and see if they equate. nodeA.val == nodeB.val ? True : False
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, l , r) -> bool:
        if(l == None and r == None):
            return True
        elif (l == None or r == None):
            return False
        # elif(l.val == r.val):
        #     print("l is " + str(l.val))
        #     print("r is " + str(r.val))
        #     return True
        # Insert last elif condition into last return statement to avoid returning True without                 calling recursive function on subtrees!!!
        return  (l.val == r.val) \
                and self.rec(l.left, r.right) \
                and self.rec(l.right, r.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.rec(root.left, root.right)