class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mp=0
        '''for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                p = prices[j]-prices[i]
                if p>mp:
                    mp = p
        return mp'''
        minp=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            else:
                profit = prices[i] - minp
                if profit>mp:
                    mp = profit
        return mp





        