class Solution:
    def decodeString(self, s: str) -> str:
        # Base case: no brackets → return as is
        if '[' not in s:
            return s
        
        for i, ch in enumerate(s):
            if ch == ']':
                # Find the matching '['
                j = i
                while s[j] != '[':
                    j -= 1
                inner = s[j+1:i]          # string between [ and ]
                
                # Find the number before '['
                k = j - 1
                while k >= 0 and s[k].isdigit():
                    k -= 1
                num_start = k + 1
                num = int(s[num_start:j])  # the repeat count
                
                # Build the new string with this block replaced
                new_s = s[:num_start] + inner * num + s[i+1:]
                
                # Recurse on the whole string
                return self.decodeString(new_s)