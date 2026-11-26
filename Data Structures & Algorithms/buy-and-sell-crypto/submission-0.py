class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = float("inf")
        best_profit = 0

        for p in prices:
            if p < lowest_price:
                lowest_price = p
            
            if best_profit < (p - lowest_price):
                best_profit = p - lowest_price
        
        return best_profit