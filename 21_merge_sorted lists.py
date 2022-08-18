"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

Example 1: 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Possible Solutions:
1) have an initial dummy node, set a tail pointer to it initialliy. within a while(true) loop, compare list1.val and list2.val, if list1.val <= list2.val, set tail.next = list1
then advance list1's head: list1 = list1.next, else tail.next = list2, advance list2's head: list2 = list2.next, and ofcourse advance the tail
 --> If either list becomes empty, set tail.next ->  head of list that has elements still present
 return dummy.next as the head of the new merged list. this works because dummy and tail point to the same list, but dummy points to the first index

2)can use recursion. maintain a "temp" head within each function call pointing to either list1 or list2 depending which contains the smaller value,
 call merge function on temp.next and list2
   
Edge cases{
    1) if either list is initially empty, dummy node should point to non-empty list, return dummy.next
}
Pseudo:
1)

dummy  = ListNode(0, None)
tail = dummy

while(True):
    if(list1 is None):
        tail.next = list2
        break;
    if(list2 is None):
        tail.next = list1
        break;

    if(list1.val <= list2.val):
        tail.next = list1
        list1 = list1.next
    else:
        tail.next = list2
        list2 = list2.next
    
    tail = tail.next

return dummy.next
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy  = ListNode(0, None)
        tail = dummy

        while(True):
            if(list1 is None):
                tail.next = list2
                break;
            if(list2 is None):
                tail.next = list1
                break;

            if(list1.val <= list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        return dummy.next