#!/usr/bin/python3

# https://leetcode.com/problems/roman-to-integer/description/
# difficulty: easy
# tags: string

# Problem: Given a roman numeral, convert it to an integer

# Approach:
# Store the roman values in a set and then compare from the set a with string of length n
# finding if the number in an index is greater than the following one. If so subtract
# the preceding from the present and skip by 2.


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        sum = 0
        idx = 0
        n = len(s)

        while idx < n:
            if idx < n - 1 and d[s[idx]] < d[s[idx + 1]]:
                sum += d[s[idx + 1]] - d[s[idx]]
                idx += 2
            else:
                sum += d[s[idx]]
                idx += 1
        return sum
