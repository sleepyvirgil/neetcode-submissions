class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # add each new element to a window
        # keep track of biggest number of items
        # if seen a item already seen, start moves to +1  
        # after first occurence

        # for each 
        l = 0
        seen = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            curr_len = (r - l) + 1
            if curr_len > longest:
                longest = curr_len
            seen.add(s[r])

        return longest
            
            


        

            
            


