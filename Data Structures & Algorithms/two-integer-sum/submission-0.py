class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapNums = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in mapNums:
                return [mapNums[diff], i]
            else:
                mapNums[n] = i

