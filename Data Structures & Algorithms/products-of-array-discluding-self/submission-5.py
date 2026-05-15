import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = 1
        pref_arr = [1]*len(nums)
        
        for i in range(len(nums)):
            pref_arr[i] = pref
            pref *= nums[i]
            
        
        suff = 1
        suff_arr = [1]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            suff_arr[i] = suff
            suff *= nums[i]
        return [x*y for x, y in zip(pref_arr, suff_arr)]