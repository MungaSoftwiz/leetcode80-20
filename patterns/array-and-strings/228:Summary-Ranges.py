#!usr/bin/python3

# https://leetcode.com/problems/summary-ranges/
# difficulty: easy
# tags arrray(list)
# Pattern: Simple loop

# Problem
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive)
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# Output: "a->b" if a != b, "a" if a == b

#Approach
# Make an empty array to keep track of summary ranges and index assigned 0.
# As long as the start index is less than the length of the nums array, assign start to current index(0) and continue looping.
# Then ensure that index is in bounds.
# also if the index ahead of it by one has the same value as current number + 1, it means we have no break and we increment the index.
# Then refer to output above for final step.

# Solution: TC 0(n) because the as both while loops will end when you get to end of array and index is not reassigned.
# Would be 0(n2) if you had index reassigned e.g with another index j.
#SC 0(n)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        idx = 0

        while idx < len(nums):
            start = nums[idx]
            while idx < len(nums) - 1 and nums[idx] + 1 == nums[idx + 1]:
                idx += 1
            if start != nums[idx]:
                ans.append(str(start) + '->' + str(nums[idx]))
            else:
                ans.append(str(nums[idx]))
            idx += 1
        return ans
