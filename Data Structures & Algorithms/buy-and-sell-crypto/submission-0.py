class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_buy=prices[0]

        for n in prices:
            if n<min_buy:
                min_buy=n
            
            curr_profit = n - min_buy  # aajka price - sabse sasta

            max_price=max(max_price,curr_profit)

        return max_price

prices = [10,1,5,6,7,1]
obj=Solution()
soln=obj.maxProfit(prices)
print(soln)