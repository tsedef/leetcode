"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Possible Solutions:
-Could be solved using a series of if-else statements to check whether parantheses/brackets are being closed, ensuring they are 
being closed by the same type of bracket and in the correct order... O(1) best case
-store last seen bracket and only continue loop if it is closed by the inverse. remove stored value if bracket was successfully closed. Loop... O(n) best case
    {edge cases: 
        1) if end of string contains an opening of bracket... automatically false : ()[]{ ... last character of string is string[-1] or string[length-1]
    }

Pseudo:
1)

if (str[index]) == '{'):
    if str[index + 1] == '}':
        index += 2
        continue
    else:
        return False
else if (str[index]) == '('):
    if str[index + 1] == ')':
        index += 2
        continue
    else:
        return False
else if (str[index]) == '['):
    if str[index + 1] == ']':
        index += 2
        continue
    else:
        return False

2)

last_seen = string[0]

while(last_seen):
!!!!!!!!!!!!!!!!! incorrect implementation, needs a queue or stack instead

"""

#Stack implementation
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ["(","[","{"]
        closers = [")","]","}"]
    
        #return false early if last element is an opener bracket
        if s[-1] in (openers):
            return False
        #return false early if first element is a closing bracket
        if s[0] in (closers):
            return False
        #for bracket in string s
        for x in s:
            if(x in openers):
               #opening bracket is appended onto stack
                stack.append(x)
            elif (x in closers):
                #position = index of where x resides in closers tuple (both lists have alternating brackets with the same index)
                pos = closers.index(x)
                #stack has to be not empty, the character in openers list should be equal to the last element on stack. 
                if(len(stack)> 0)and openers[pos] == stack[-1]:
                    #Pop once brackets match
                    stack.pop()
                else:
                    return False
                
        #returns true only when stack is empty.
        return not stack

        #How to improve time complexity? 
        # Runtime: 57 ms, faster than 19.74% of Python3 online submissions for Valid Parentheses.
        #Memory Usage: 13.9 MB, less than 72.54% of Python3 online submissions for Valid Parentheses.  