class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}

        for i in nums:
            hMap[i] = hMap.get(i, 0) + 1

        new_hMap = {k: v for k, v in sorted(hMap.items(), key=lambda item: item[1], reverse = True)}
        return list(new_hMap.keys())[:k]