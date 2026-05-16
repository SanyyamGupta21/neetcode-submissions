class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_res = set()

        for i in range(len(nums)):
            target = -nums[i]
            hMap = {}

            for j in range(i + 1, len(nums)):
                num = nums[j]
                diff_num = target - num

                if diff_num in hMap:
                    final_res.add(
                        tuple(sorted([nums[i], num, diff_num]))
                    )
                else:
                    hMap[num] = j

        return list(final_res)