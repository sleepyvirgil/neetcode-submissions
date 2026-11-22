class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #pre and post arrays
        n = len(nums)
        pre = [0] * n
        post = [0] * n

        for i in range(n):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                post[i] = 1
            else: 
                post[i] = post[i + 1] * nums[i + 1]

        output = [0] * n
        for i in range(n):
            output[i] = pre[i] * post[i]
        
        return output

        # nums: 1   2 3 4
        # pre:  1   1 2 6
        # post: 24 12 4 1
        # output: 24 12 8 6



                

