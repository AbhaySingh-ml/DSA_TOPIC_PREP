# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Step 1: Check if lengths of s and t are same
# Step 2: Create empty dict for s_count
# Step 3: Create empty dict for t_count
# Step 4: Loop through each character in s and update s_count
# Step 5: Loop through each character in t and update t_count
# Step 6: Compare both dictionaries

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Create dictionaries to count characters
        s_count = {}
        t_count = {}

        # Step 3: Count characters in s
        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1

        # Step 4: Count characters in t
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1

        # Step 5: Compare the dictionaries
        return s_count == t_count
