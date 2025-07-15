class solution():
    def two_sum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = num - target
            if complement in num_map:
                return[num[complement], i]

# buy and sell stocks 
# Step 1 := Frist make a array that will take input of the int as an array.
# Step 2 :- Look the the minimum int (element) in the array.(buy)
# step 3 :- Loop for the maximum int (element) in the array.(sell)
# step 4 :- index 0 means day 1

# Initialize a variable to track the minimum price seen so far
# Initialize a variable to track the maximum profit

# Loop through each price in the prices array
    # If the current price is less than the minimum price so far, update the minimum price
    # Else, calculate the profit by subtracting min price from current price
    # If this profit is greater than max profit so far, update max profit

# Return the max profit
 








