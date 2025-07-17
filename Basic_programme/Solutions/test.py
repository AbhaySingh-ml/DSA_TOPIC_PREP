# class solution:
#     def sum_of_digit(self, num: int) ->int:
#         total = 0
#         while num > 0 :
#             total += num % 10
#             num //= 10
#         return total



# class solution:
#     def reverse_digit(self, num: int) ->int
#     for i in range(num):
#         reverse = num % 10
#         return reverse

        # class solution:
#     def sum_of_digit(self, num: int) ->int:
#         total = 0
#         while num > 0 :
#             total += num % 10
#             num //= 10
#         return total



# class solution:
#     def reverse_digit(self, num: int) ->int
#     for i in range(num):
#         reverse = num % 10
#         return reverse

# class solution:
#     def count_digit(self, num: int):
#         for i in range(num):
#             count = num // 10

# class solution:
#     def count_digit(self, num: int):
#         while num > 0:
#             count = num // 10
#             count +1

# class solution:
#     def count_digit(self, num: int):
#         count = 0
#         if num == 0:
#             return 1
        
#     while num > 0:
#         num = num // 10
#         count +=1
#     return count    

# for 

# class solution:
#     def sum_of_digit(self, num: int):
#         sum = 0 
#         while num > 0:
#             num = num // 10
#             sum += 1
#         return sum


'''Q4. Check for Palindrome Number
Check if the number reads the same forward and backward.
Example: Input: 121 → Output: True, Input: 123 → Output: False
'''
# class solution:
#     def palindrome(self, num: int):
#         # edge case
#         if num == 0:
#         #   if the input is 0 this will treat not a plaindrome
#           return False 
#         while num > 0:
#            last_digit = 0
#            last_digit = num % 10
           
"""
Q5. Find the Largest Digit
Return the largest digit in a number.
Example: Input: 4723 → Output: 7
"""          
# class solution:
#     def largest_digit(self, num: int):
#         if num == 0:
#             return 0
#         while num > 0:
#             # extract every digit from the number 
#             # and then campare then in this while loop
#             digit = num % 10

'''
Q6. Sum of Even Digits
Take a number and return the sum of only the even digits.
Example: Input: 123456 → Output: 2 + 4 + 6 = 12
'''
# class solution:
#     def sum_of_even_digit(self, num: int):
#         # take out the single digit from the number 
#         # check the divisiblity by 2 
#         # if the remainder is 0 and add them
#         while num > 0:
#             single_digit = num % 10
#             check_even = single_digit / 2
#             if check_even == 0:
#                 # add all the digit with reminder 0 
#                 # but i dont know how to code it
#             else:
#                 # this is the case of odd digit in the number leave this number
#                 # do nothing here
#                 # break
#                 return check_even
            
'''
Q7. Check if Number is Armstrong
Check if a 3-digit number is an Armstrong number.¶
(Armstrong = sum of cubes of digits equals the number)
Example: Input: 153 → Output: True (1³ + 5³ + 3³ = 153)
'''
# class solution:
#     def armstrong(self, num: int):
#         while num > 0:
#             digit = num % 10
#             Square = digit * digit 
#             new_num += Square
#         return num == new_num
    
    # tell me the correction and accuracy with this code and tell me the correct solution 

'''
Q8. Count Occurrences of a Digit
Count how many times a digit (say 5) appears in a number.
Example: Input: 15525, Digit: 5 → Output: 3
'''
class solution:
    def count(self, num: int):
        while num > 0:
            digit = num % 10
            num = num // 10 
            if digit == digit:
                return num
            else:
                


    # tell me the correction and accuracy with this code and tell me the correct solution 