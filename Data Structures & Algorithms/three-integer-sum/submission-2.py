class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort nums
        # starting from negatives (or 0) 
        # continue on if number is the same as previous 
        # partition rest of right side array into 
        # two pointer with target being abs of initial number
        # if found, keep looking inward from interval for another solu
    
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                return res
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i + 1, n - 1

            while lo < hi:
                if nums[i] + nums[lo] + nums[hi] == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif nums[i] + nums[lo] + nums[hi] < 0:
                    lo += 1
                else:
                    hi -= 1
                
        return res
