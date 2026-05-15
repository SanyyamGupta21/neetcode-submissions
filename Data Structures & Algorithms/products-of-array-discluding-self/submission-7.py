class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = 1
        pref_arr = [1]*len(nums)
        
        for i in range(len(nums)):
            pref_arr[i] = pref
            pref *= nums[i]
            
        
        suff = 1
        for i in range(len(nums)-1, -1, -1):
            pref_arr[i] *= suff
            suff *= nums[i]
        return pref_arr