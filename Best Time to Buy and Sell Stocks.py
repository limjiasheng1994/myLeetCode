class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        else:
            highestProfit = 0

            def checkProfit(buy, sell: List[int]):
                result = False
                if max(sell) > buy:
                    result = max(sell) - buy
                return result
            
            for i in range(0, len(prices)-1):
                buy = prices[i]
                sell = prices[i+1:]
                if checkProfit(buy, sell) != False and checkProfit(buy, sell) > highestProfit:
                    highestProfit = checkProfit(buy, sell)
                    
            return highestProfit