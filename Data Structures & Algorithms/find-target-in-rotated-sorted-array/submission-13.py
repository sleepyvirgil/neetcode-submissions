class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array nums, int target
        # return index of target, -1 if not present
        # binary search 

        # [3,4,5,6,1,2]
        # [1,2,3,4,5,6]
        # figure out which half target is in
        # binary search on that half

        # binary search for smallest element
        # 
        # nums[0] > target, bin search right side
        # nums[0] < target, bin search the left side 

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        ind_small = l
        if target > nums[-1]:
            i, j = 0, (ind_small - 1)
        else:
            i, j = ind_small, len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1
            
        return -1
