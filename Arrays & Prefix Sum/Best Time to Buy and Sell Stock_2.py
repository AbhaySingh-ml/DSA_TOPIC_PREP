'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, 
you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

'''
# Initialize a variable to track the minimum price seen so far
# Initialize a variable to track the maximum profit

# Loop through each price in the prices array
    # If the current price is less than the minimum price so far, update the minimum price
    # Else, calculate the profit by subtracting min price from current price
    # If this profit is greater than max profit so far, update max profit

# Return the max profit
'''
# how to sovle for buy and sell for part 1
prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf')  # Track the lowest price seen so far
max_profit = 0            # Track the highest profit so far

for price in prices:
    if price < min_price:
        min_price = price  # Found a new lower buying price
    profit = price - min_price  # Potential profit if sold today
    if profit > max_profit:
        max_profit = profit  # Update max profit if this one is higher

print(max_profit)  # Output the result


'''
# part 2
function maxProfit(prices):
    initialize total_profit to 0

    for i from 1 to length of prices - 1:
        if prices[i] > prices[i - 1]:  # if today's price is higher than yesterday's
            profit = prices[i] - prices[i - 1]
            add profit to total_profit

    return total_profit
'''
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # Buy yesterday and sell today if today's price is higher
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# Example
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 7 (Buy at 1, sell at 5; buy at 3, sell at 6)

