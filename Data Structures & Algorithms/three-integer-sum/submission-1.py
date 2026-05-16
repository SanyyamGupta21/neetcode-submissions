class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_res = set()

        neg_nums = [-x for x in nums]
        for i, target in enumerate(neg_nums):
            hMap = {}
            for j, num in enumerate(nums[i+1:]):
                diff_num = target - num
                if diff_num in hMap:
                    final_res.add(tuple(sorted([-target,num,diff_num])))
                else:
                    hMap[num] = j

        return list(final_res)