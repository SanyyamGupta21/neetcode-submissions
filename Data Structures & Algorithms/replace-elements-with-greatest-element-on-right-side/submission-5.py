class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
         
        if len(arr) == 1:
            return [-1]
        j = 0
        for i in range(len(arr)):
            max_num = max(arr[j+1:])
            if arr[i] == max_num:
                arr[j:i] = [max_num]*(i-j)
                j = i
        arr[-1] = -1
        return arr