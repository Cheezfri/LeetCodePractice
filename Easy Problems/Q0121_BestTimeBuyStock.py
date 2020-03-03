import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = sys.maxsize
        for price in prices:
            if -min_value + price > max_profit:
                max_profit = -min_value + price
            if price < min_value:
                min_value = price
        return max_profit


if __name__ == "__main__":
    ans = Solution.maxProfit(Solution, [7, 1, 5, 3, 6, 4])
    print(ans)
'''
Prompt:
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one

Notes:
use "sys.maxsize" when initializing a minimum value variable
Logically, you only need to know the lowest value you can buy a stock, then after that you can compute
    the profit of the lowest value bought - the current day you are on until you reach the end of the loop
    Only one loop, therefore O(n)
'''
