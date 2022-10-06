class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Loop through and get lowest value
        # Loop remaining to get highest value
        # return price diff

        # lowest = 1000
        # index = 0
        # highest = 0
        # for i in range (0, len(prices)):
        #     if prices[i] < lowest:
        #         lowest = prices[i]
        #         index = i
        # for i in range (index, len(prices)):
        #     if prices[i] > highest:
        #         highest = prices[i]
        #         index = i
        # print(lowest, highest)
        # return highest - lowest

        # sliding pointers
        # left pointer moves up to right if lower
        # right pointer moves up until reaches the end
        # calc profit and compare if its higher
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            elif maxProfit < prices[right] - prices[left]:
                maxProfit =  prices[right] - prices[left]
            right += 1
        return maxProfit
            
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))