class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # bucket sort letters for freq
        # loop through 
        # add element to requency matrix
        # can treat k as a buffer for different element
        # while loop check if (window size) - max(a) > k
        #   subtract 1 from letter that is currently at l, move l by 1
        # check if length is greater than longest
        # return longest


        l = 0
        longest = 0
        a = [0] * 26

        for r in range(len(s)):
            # add element to freq array
            a[ord(s[r]) - ord("A")] += 1

            # invalid if window - max(a) > k 
            while (r - l + 1) - max(a) > k:
                a[ord(s[l]) - ord("A")] -= 1
                l += 1

            # check longest window
            longest = max((r - l + 1), longest)

        return longest
            

            
            
