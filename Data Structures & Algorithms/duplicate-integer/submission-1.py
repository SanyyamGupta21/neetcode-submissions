class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums:
            if i in hmap:
                return True
            hmap[i] = hmap.get(i,0) + 1
        return False