class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # water calculation = W * H = (r - l) * min(h[l], h[r])
        n = len(heights)
        max_area = 0
        l = 0
        r = n - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > max_area:
                max_area = area
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
