class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = maxPrice = prices[0]
        totalProfit = 0
        profit = 0
        for i in range(1, len(prices)):
            if profit != 0 and prices[i] < maxPrice:    
                totalProfit += profit
                profit = 0
                minPrice = maxPrice = prices[i]
            elif minPrice > prices[i]:
                minPrice = maxPrice = prices[i]
            elif maxPrice < prices[i]:
                maxPrice = prices[i]
                profit = maxPrice - minPrice

        totalProfit += profit
        return totalProfit
