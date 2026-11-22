class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # store every element in a set
        # check if a number is the beginning of a sequence
        # if yes, find how long that sequence is, keep track 

        s = set(nums)
        longest = 0
        for n in s:
            if n - 1 in s:
                continue
                
            length = 1
            next_num = n + 1
            while next_num in s:
                length += 1
                next_num += 1
            longest = max(longest, length)

        return longest
            

    
