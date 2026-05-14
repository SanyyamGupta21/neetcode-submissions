class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []

        for i, num in enumerate(nums):
            others = nums[:i] + nums[i+1:]

            prod = 1
            for x in others:
                prod *= x
            new_arr.append(prod)
        return new_arr