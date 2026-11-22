class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # store every element in a set
        # check if a number is the beginning of a sequence
        # if yes, find how long that sequence is, keep track 

        s = set(nums)
        longest = 0
        for n in nums:
            if n - 1 in s:
                continue
            else:
                length = 0
                while n in s:
                    length += 1
                    n += 1
                if length > longest:
                    longest = length

        return longest
            

    
