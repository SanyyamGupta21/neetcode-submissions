class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while n/2 > 1:
            n = n/2
        if n/2 == 1:
            return True
        return False