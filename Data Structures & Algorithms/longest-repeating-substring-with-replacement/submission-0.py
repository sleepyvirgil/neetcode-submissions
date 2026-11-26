class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        a = [0] * 26

        for r in range(len(s)):
            a[ord(s[r]) - ord("A")] += 1
            
            while ((r - l) + 1) - max(a) > k:
                a[ord(s[l]) - ord("A")] -= 1
                l += 1

            w = (r - l) + 1
            if w > longest:
                longest = w

        return longest
            

            
            
