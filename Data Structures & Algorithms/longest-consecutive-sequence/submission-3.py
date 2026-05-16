class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_len = 0
        for num in nums:
            length = 0
            if (num - 1) in nums:
                continue
            length += 1

            while length <= len(nums):
                if (num + length) in nums:
                    length +=1
                else:
                    max_len = max(max_len, length)
                    break
        return max_len