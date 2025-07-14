# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of the two numbers
            num_map[num] = i  # Store index of current number

# Example usage:
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # Output: [0, 1]
print(solution.twoSum([3,2,4], 6))  # Output: [1, 2]
print(solution.twoSum([3,3], 6))  # Output: [0, 1]