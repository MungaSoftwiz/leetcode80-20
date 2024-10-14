#!/usr/bin/python3

# https://leetcode.com/problems/is-subsequence/description/
# difficulty: easy
# tags: string, two pointers

# Problem
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# Approach
# Have a two pointers for the string and subsequence string.
# Loop through the string while comparing it with the subsequence string until they both deplete

# Solution: O(n) for Tc and O(1) for Sc

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        x = 0

        if s == '': return True
        if S > T: return False

        for y in range(T):
            if s[x] == t[y]:
                if x == S - 1:
                    return True
                x += 1
        return False
