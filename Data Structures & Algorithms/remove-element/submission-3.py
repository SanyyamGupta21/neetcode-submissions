class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                counter += 1
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return len(nums) - counter
