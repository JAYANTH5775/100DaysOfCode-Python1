---
description: >-
  Given a binary array nums and an integer goal, return the number of non-empty
  subarrays with a sum goal.  A subarray is a contiguous part of the array
---

# Binary Subarrays With Sum

````python
// Some code```python3
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        res = defaultdict(int)

        res[0] = 1

        prefixsum =0

        ans =0 

        for i in nums: 
            prefixsum+=i
            ans+=res[prefixsum-goal]
            res[prefixsum] +=1
        return ans

        

        # target_sum = 0 
        # count =0 

        # for i in range(len(nums)):

        #     for j in range(i , len(nums)):
        #         target_sum = nums[i:j+1].count(1)
        #         if target_sum == goal:
        #             count+=1
        # return count


```
````
