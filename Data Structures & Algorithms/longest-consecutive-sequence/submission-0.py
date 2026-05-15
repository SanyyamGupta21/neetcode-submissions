class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new_nums = sorted(set(nums))

        seq_count = 1
        max_seq = 1
        start_num = new_nums[0]

        for i in range(1, len(new_nums)):
            if start_num + 1 == new_nums[i]:
                seq_count += 1
                start_num = new_nums[i]
            else:
                max_seq = max(seq_count, max_seq)
                seq_count = 1
                start_num = new_nums[i]
        return max(seq_count, max_seq)