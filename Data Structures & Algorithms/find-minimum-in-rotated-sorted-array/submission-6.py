class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # [3,4,5,6,1,2]
        # [big|small]
        # nums[r] is the smallest element we know so far
        # comparing to nums[l] doesnt work in sorted case
        # comparing nums[mid] against nums[r] tells which side mid is on
        # bigger than nums[r], smallest is on right side, left up to mid inc. partitioned off
        # smaller than nums[r], smallest is on right, could be mid, right partitioned off

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (r + l) // 2

        # [3,4,5,6,1,2]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[r]



