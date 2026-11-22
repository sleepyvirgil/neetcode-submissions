class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output array in place
        n = len(nums)
        output = [0] * n

        for i in range(n):
            if i == 0:
                output[i] = 1
            else: 
                output[i] = output[i - 1] * nums[i - 1]
        
        post = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * post
            post = post * nums[i]
        
        return output


        # nums: 1  2   4 6     # post: 1, 6, 24, 48
        # out:  1  1   2 8
        #      48  24  12  8
