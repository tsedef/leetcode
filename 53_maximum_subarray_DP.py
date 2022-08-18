"""
Dynamic Programming Problem!!!

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Possible Solutions:
1) Cubic or Quadratic time. 
    - int n = length of nums array
    - int max_subarray_sum = initialize to minimum value of an integer
    - outerloop is lowerbound (left), increment only after visiting every other element within inner loop(window)
    - innerloop is right (left + 1) initially. adds nums[right] to previously computed value to get subarray sum (variable: running_window_sum)
    - within innerloop check if the window beats the best sum already seen!!!
        :: max_subarray_sum = max(max_subbaray_sum, running_window_sum) 
    
"""

#Cubic:
class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''
        n = len(nums)
        # Arbitrary minimum value for python
        max_sum = -10000
        
        """
        We will use these outer 2 for loops to investigate all
        windows of the array.
      
        We plant at each 'left' value and explore every
        'right' value from that 'left' planting.

        These are our bounds for the window we will investigate.
        """
        for left in range(0, n):
            for right in range(left, n):
                # Let's investigate this window
                window_sum = 0

                # Add all items in the window
                for k in range(left, right + 1):
                    window_sum += nums[k]

                # Did we beat the best sum seen so far?
                max_sum = max(max_sum, window_sum)

        return max_sum

#Quadratic:
class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''
        n = len(nums)
        # Arbitrary minimum value for python
        max_sum = -1000000000

        # Left will be the starting index of subarray
        for left in range(0, n):
            running_sum = 0
            # Right will be the ending index of subarray
            for right in range(left, n):

                # Add the current element to previous computed value
                # To get the subarray sum
                running_sum += nums[right]
                
                # Does this window beat the best sum we have seen so far?
                max_sum = max(max_sum, running_sum)

        return max_sum

#Linear:
class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''
        
        """
        We default to say the the best maximum seen so far is the first
        element.

        We also default to say the the best max ending at the first element
        is...the first element.
        """
        max_so_far = nums[0]
        max_ending_here = nums[0]
            
        # We will investigate the rest of the items in the array from index 1 onward.
        for i in range(1, len(nums)):
            """
            We are inspecting the item at index i.
    
            We want to answer the question:
            "What is the Max Contiguous Subarray Sum we can achieve ending at index i?"
    
            We have 2 choices:
    
            maxEndingHere + nums[i] (extend the previous subarray best whatever it was)
              1.) Let the item we are sitting at contribute to this best max we achieved
              ending at index i - 1.
    
            nums[i] (start and end at this index)
              2.) Just take the item we are sitting at's value.
    
            The max of these 2 choices will be the best answer to the Max Contiguous
            Subarray Sum we can achieve for subarrays ending at index i.
    
            Example:
    
            index     0  1   2  3   4  5  6   7  8
            Input: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
                     -2, 1, -2, 4,  3, 5, 6,  1, 5    'maxEndingHere' at each point
            
            The best subarrays we would take if we took them:
              ending at index 0: [ -2 ]           (snippet from index 0 to index 0)
              ending at index 1: [ 1 ]            (snippet from index 1 to index 1) [we just took the item at index 1]
              ending at index 2: [ 1, -3 ]        (snippet from index 1 to index 2)
              ending at index 3: [ 4 ]            (snippet from index 3 to index 3) [we just took the item at index 3]
              ending at index 4: [ 4, -1 ]        (snippet from index 3 to index 4)
              ending at index 5: [ 4, -1, 2 ]     (snippet from index 3 to index 5)
              ending at index 6: [ 4, -1, 2, 1 ]  (snippet from index 3 to index 6)
              ending at index 7: [ 4, -1, 2, 1, -5 ]    (snippet from index 3 to index 7)
              ending at index 8: [ 4, -1, 2, 1, -5, 4 ] (snippet from index 3 to index 8)
    
            Notice how we are changing the end bound by 1 everytime.
            """
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            
            # Did we beat the 'maxSoFar' with the 'maxEndingHere'?
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far
        
        