class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array nums, int target
        # return index of target, -1 if not present
        # binary search 

        # [3,4,5,6,1,2]
        # [1,2,3,4,5,6]
        # figure out smallest element
        # if target is bigger than smallest, bin search right side (smallest inclu)
        # else bin search left side

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else: # nums[mid] > nums[r]
                l = mid + 1           
        smallest_ind = r

        if target > nums[-1]: # left side
            i, j = 0, smallest_ind - 1
        else: # target < nums[-1]
            i, j = smallest_ind, len(nums) - 1
        
        while i <= j:
            m = (i + j) // 2

            if target == nums[m]:
                return m
            elif nums[m] < target:
                i = m + 1
            else: # target < nums[m]
                j = m - 1
        
        return -1



                

        