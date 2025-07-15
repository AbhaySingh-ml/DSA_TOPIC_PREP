# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.
# logic to solve this problem

prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf')
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

print("Maximum Profit:", max_profit)
'''
# Initialize a variable to track the minimum price seen so far
# Initialize a variable to track the maximum profit

# Loop through each price in the prices array
    # If the current price is less than the minimum price so far, update the minimum price
    # Else, calculate the profit by subtracting min price from current price
    # If this profit is greater than max profit so far, update max profit

# Return the max profit
'''

# Acutal leetcode solution
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
