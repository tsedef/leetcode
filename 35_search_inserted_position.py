"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6,8,10,13], target = 10
Output: 5

Input: nums = [1,3,5,6,8,11,13], target = 10
Output: 5

Possible Solutions: O(log n) RUNTIME!
1)binary search tree...
    -check middle element of array and create an "index pointer" for that element's pos, if target > mid, search right side; else search left side
    -depending on whether you're in the right or left side of array, increment/decrement index pointer while simultaneously comparing target and element. 
        ++if you come across an element that is greater/smaller than target without first finding target, return index pointer
        ++if element is found, you still return index pointer (bc it is simultaneously changed)

Edge cases{
    1) if list empty, return 0
    2) target would be first or last element instantied in list 
}

Pseudo:

if(nums is None):
    return 0

mid = nums[len(nums)//2] #floored division
idx  = nums.index(mid)

if(target == mid):
    return idx

if(target > mid):
    idx +=1
    for num in nums[mid:]:
        if(target == num):
            return idx
        elif(target < num):
            return idx
        idx +=1
    return idx

else:
     idx -=1
    for num in nums[:mid]:
        if(target == num):
            return idx
        elif(target > num):
            return idx
        idx -=1
    return idx
-----------------------
CORRECT SOLUTION
left = 0 #start of list
right = len(nums) - 1 #end of list

while left <= right:
    middle = left + (right - left) // 2 #middle element initially and after every half of list
    if(nums[middle] < target): # halve list towards right side (larger elements) by making middle + 1 the left (lower) bound
        left = middle + 1
    elif(nums[middle] > target):  # halve list towards left side (small elements) by making middle the right (upper) bbound
        right = middle - 1
    elif(nums[middle] == target): # target is found
        return middle
return left # target was not found, left determines where it would be inserted

"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums is None):
            return 0
        
        left = 0 #start of list
        right = len(nums) - 1 #end of list

        while left <= right:
            middle = left + (right - left) // 2 #middle element initially and after every half of list
            if(nums[middle] < target): # halve list towards right side (larger elements) by making middle + 1 the                                            left (lower) bound
                left = middle + 1
            elif(nums[middle] > target):  # halve list towards left side (small elements) by making middle the right                                             (upper) bound
                right = middle - 1
            elif(nums[middle] == target): # target is found
                return middle
        
        return left # target was not found, left determines where it would be inserted