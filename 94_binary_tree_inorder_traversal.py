"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

Example 1:
    1 
        2
    3

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Possible Solutions: INORDER  Left -> Root -> Right
1) Recursion
- Traverse left until there is a node with no left children, then append root and that node's right child.
- Apply the same function if the node's right child has children. (traverse all the way left)
- Work your way back up the left side to root and apply same function to right side

2) Iterative STACK
    1) Create an empty stack S.
    2) Initialize current node as root
    3) Push the current node to S and set current = current->left until current is NULL
    4) If current is NULL and stack is not empty then 
        a) Pop the top item from stack.
        b) Print the popped item, set current = popped_item->right 
        c) Go to step 3.
    5) If current is NULL and stack is empty then we are done.

Pseudo:
1)

def inorderTraversal(root):
    if(root != None):
        inorderTraversal(root.left)
        lstOfNodes.append(root.val)
        inorderTraversal(root.right)
    
    return lstOfNodes

2)
# A binary tree node
class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Iterative function for inorder tree traversal
def inOrder(root):
	
	# Set current to root of binary tree
	current = root
	stack = [] # initialize stack
	
	while True:
		
		# Reach the left most Node of the current Node
		if current is not None:
			
			# Place pointer to a tree node on the stack
			# before traversing the node's left subtree
			stack.append(current)
		
			current = current.left

		
		# BackTrack from the empty subtree and visit the Node
		# at the top of the stack; however, if the stack is
		# empty you are done
		elif(stack):
			current = stack.pop()
			print(current.data, end=" ") # Python 3 printing
		
			# We have visited the node and its left
			# subtree. Now, it's right subtree's turn
			current = current.right

		else:
			break
	
	print()

# Driver program to test above function

 Constructed binary tree is
			1
		/ \
		2	 3
	/ \
	4 5  

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right'

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst_nodes = []   
        if(root is not None):
            lst_nodes = self.inorderTraversal(root.left)
            lst_nodes.append(root.val)
            lst_nodes = lst_nodes + self.inorderTraversal(root.right)
        return lst_nodes