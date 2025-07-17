# class solution():
#     def two_sum(self, nums, target):
#         num_map = {}
#         for i, num in enumerate(nums):
#             complement = num - target
#             if complement in num_map:
#                 return[num[complement], i]

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
 


'''
Two pointers question
Given a sorted list of integers, remove the duplicates in-place such that each element appears only once
and return the new length.
Do not use extra space for another list — 
you must do this by modifying the original list in-place with O(1) extra memory.
'''
# input_num = list(map(int, input().split()))
# for element in input_num(num):
#     if num in input_num:
#         return input_num
#     else:


nums = list(map(int, input("Enter sorted numbers: ").split()))

i = 0  # This is where we place the next unique number
for j in range(1, len(nums)):
    if nums[j] != nums[i]:  # Found a new unique number
        i += 1              # Move i to next position
        nums[i] = nums[j]   # Overwrite it with the new unique number

# i + 1 is the length of unique elements
print("Length after removing duplicates:", i + 1)
print("Modified list:", nums[:i+1])







