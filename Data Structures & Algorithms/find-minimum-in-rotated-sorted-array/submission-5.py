class Solution:
    def findMin(self, nums: List[int]) -> int:

        # [3,4,5,6|1,2]
        # [1,2,3,4,5,6]
        # [bigger|smaller
        # each number in bigger > last element in smaller
        # if nums[mid] > nums[r]
        # move l to mid + 1


        l = 0
        r = len(nums) - 1
    
        while l < r:
            mid = (r + l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        return nums[l]

