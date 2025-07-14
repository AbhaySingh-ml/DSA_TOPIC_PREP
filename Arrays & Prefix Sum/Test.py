class solution():
    def two_sum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = num - target
            if complement in num_map:
                return[num[complement], i]


