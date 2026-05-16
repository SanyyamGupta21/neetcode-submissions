class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_res = []

        neg_nums = [-x for x in nums]
        for i, target in enumerate(neg_nums):
            hMap = {}
            for j, num in enumerate(nums[i+1:]):
                diff_num = target - num
                if diff_num in hMap:
                    final_res.append([-target,num,diff_num])
                else:
                    hMap[num] = j

        return list({tuple(sorted(subarr)): subarr for subarr in final_res}.values())


        