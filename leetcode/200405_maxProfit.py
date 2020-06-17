class Solution:
    def maxProfit(self, prices):
        total = 0
        if len(prices) < 1: return total
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total
        
nums = [7,1,5,3,6,4]
sol = Solution()
nums = sol.maxProfit(nums)
print(nums)